from tkinter import Toplevel, Label, Entry, Button, StringVar, BooleanVar
import text_formatting

search_window = None
occurrences_var = None
case_sensitive = None
current_occurrence = 0
search_term = ""


def search_popup(root):
    global search_window, occurrences_var, case_sensitive
    if search_window is not None and search_window.winfo_exists():
        search_window.lift()
        return

    search_window = Toplevel(root)
    search_window.title("Search")
    search_window.geometry("400x100")
    search_window.attributes("-topmost", True)
    search_window.protocol("WM_DELETE_WINDOW", on_search_window_close)

    search_entry = Entry(search_window)
    search_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    search_entry.focus_set()
    search_entry.bind("<KeyRelease>", lambda e: search_text(search_entry.get(), None))

    occurrences_var = StringVar()
    Label(search_window, textvariable=occurrences_var).grid(
        row=1, column=2, columnspan=2, padx=10, pady=10
    )

    Button(
        search_window,
        text="Find Next",
        command=lambda: search_text(search_entry.get(), "next"),
    ).grid(row=1, column=0, padx=10, pady=10)
    Button(
        search_window,
        text="Find Previous",
        command=lambda: search_text(search_entry.get(), "previous"),
    ).grid(row=1, column=1, padx=10, pady=10)

    case_sensitive = BooleanVar(root, False)
    case_sensitive_button = Button(
        search_window,
        text="Case Sensitive",
        command=lambda: toggle_case_sensitive(
            case_sensitive_button, search_entry.get()
        ),
    )
    case_sensitive_button.grid(row=0, column=2, columnspan=1, padx=10, pady=10)
    update_case_sensitive_button(case_sensitive_button)

    # Bind text changes
    text_formatting.text_area.bind(
        "<KeyRelease>", lambda e: on_text_modified(search_entry)
    )

    # Check if text is selected in the text area, and use it as the search query
    selected_text = (
        text_formatting.text_area.get("sel.first", "sel.last")
        if text_formatting.text_area.tag_ranges("sel")
        else ""
    )
    search_query = selected_text if selected_text else search_entry.get()
    search_entry.delete(0, "end")
    search_entry.insert(0, search_query)
    search_text(search_query, None)


def on_text_modified(search_entry):
    # Reset search when text is modified
    text_formatting.text_area.edit_modified(False)
    search_text(search_entry.get(), None)


def on_search_window_close():
    global search_window, current_occurrence, search_term
    # unbind text changes
    text_formatting.text_area.unbind("<KeyRelease>")
    text_formatting.text_area.tag_remove("found", "1.0", "end")
    text_formatting.text_area.tag_remove("current_found", "1.0", "end")
    search_window.destroy()
    search_window = None
    current_occurrence = 0
    search_term = ""


def search_text(word, direction):
    global current_occurrence, search_term
    text_area = text_formatting.text_area

    if not word:
        text_area.tag_remove("found", "1.0", "end")
        text_area.tag_remove("current_found", "1.0", "end")
        occurrences_var.set("")
        return

    # Reset search only if the word changes
    if word != search_term:
        search_term = word
        current_occurrence = 0

    text_area.tag_remove("found", "1.0", "end")
    text_area.tag_remove("current_found", "1.0", "end")

    occurrences = []
    start_pos = "1.0"

    while True:
        start_pos = text_area.search(
            word, start_pos, stopindex="end", nocase=not case_sensitive.get()
        )
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(word)}c"
        text_area.tag_add("found", start_pos, end_pos)
        occurrences.append(start_pos)
        start_pos = end_pos

    text_area.tag_config("found", background="orange")

    count = len(occurrences)
    if count == 0:
        occurrences_var.set("No results")
        return

    # Determine current occurrence based on cursor position
    cursor_pos = text_area.index("insert")
    for i, pos in enumerate(occurrences):
        if text_area.compare(cursor_pos, "<", pos):
            current_occurrence = i if direction == "next" else max(i - 1, 0)
            break
    else:
        current_occurrence = count - 1 if direction == "previous" else 0

    if direction == "next":
        current_occurrence = (current_occurrence) % count
    elif direction == "previous":
        current_occurrence = (current_occurrence - 1) % count

    # Highlight current occurrence
    if direction in ["next", "previous"]:
        pos = occurrences[current_occurrence]
        end_pos = f"{pos}+{len(word)}c"
        text_area.tag_add("current_found", pos, end_pos)
        text_area.mark_set("insert", end_pos)

        text_area.see(pos)
        text_area.tag_config("current_found", background="lightgreen")

    # Update label
    occurrences_var.set(f"{current_occurrence + 1} of {count}")


def toggle_case_sensitive(button, word):
    case_sensitive.set(not case_sensitive.get())
    update_case_sensitive_button(button)
    search_text(word, None)


def update_case_sensitive_button(button):
    button.config(fg="blue" if case_sensitive.get() else "black")
