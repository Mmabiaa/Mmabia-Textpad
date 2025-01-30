from tkinter import Toplevel, Label, Entry, Button, StringVar, BooleanVar
import text_formatting


class SearchWindow:
    # Class-level variable to track the active window
    search_window_instance = None

    def __init__(self, root):
        if SearchWindow.search_window_instance:
            # If there's already an open search window, bring it to the front
            SearchWindow.search_window_instance.search_window.lift()
            # Focus on the search entry
            SearchWindow.search_window_instance.search_entry.focus_set()
            # Check if text is selected in the text area, and use it as the search query
            SearchWindow.search_window_instance.on_selected_area_text()
            return

        self.search_window = Toplevel(root)
        self.occurrences_var = StringVar()
        self.case_sensitive = BooleanVar(root, False)
        self.current_occurrence = 0
        self.search_term = ""
        self.text_area = text_formatting.text_area
        self.search_entry = Entry(self.search_window)
        self.create_popup()

        # Assign this instance to the class-level variable
        SearchWindow.search_window_instance = self

    def create_popup(self):

        self.search_window.title("Search")
        self.search_window.geometry("400x100")
        self.search_window.attributes("-topmost", True)
        self.search_window.protocol("WM_DELETE_WINDOW", self.on_search_window_close)

        self.search_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.search_entry.focus_set()
        self.search_entry.bind(
            "<KeyRelease>", lambda e: self.search_text(self.search_entry.get(), None)
        )

        Label(self.search_window, textvariable=self.occurrences_var).grid(
            row=1, column=2, columnspan=2, padx=10, pady=10
        )

        Button(
            self.search_window,
            text="Find Next",
            command=lambda: self.search_text(self.search_entry.get(), "next"),
        ).grid(row=1, column=0, padx=10, pady=10)
        Button(
            self.search_window,
            text="Find Previous",
            command=lambda: self.search_text(self.search_entry.get(), "previous"),
        ).grid(row=1, column=1, padx=10, pady=10)

        case_sensitive_button = Button(
            self.search_window,
            text="Case Sensitive",
            command=lambda: self.toggle_case_sensitive(
                case_sensitive_button, self.search_entry.get()
            ),
        )
        case_sensitive_button.grid(row=0, column=2, padx=10, pady=10)
        self.update_case_sensitive_button(case_sensitive_button)

        # Bind text changes
        self.text_area.bind("<KeyRelease>", lambda e: self.on_text_modified())
        self.on_selected_area_text()  # Move this call to the end of create_popup()

    def on_selected_area_text(self):
        # Check if text is selected in the text area, and use it as the search query
        selected_text = (
            self.text_area.get("sel.first", "sel.last")
            if self.text_area.tag_ranges("sel")
            else ""
        )
        search_query = selected_text if selected_text else self.search_entry.get()
        self.search_entry.delete(0, "end")
        self.search_entry.insert(0, search_query)

        # Ensure the search updates with the new text
        self.search_text(search_query, None)

    def on_text_modified(self):
        # Reset search when text is modified
        self.text_area.edit_modified(False)
        self.search_text(self.search_entry.get(), None)

    def on_search_window_close(self):
        # unbind text changes
        self.text_area.unbind("<KeyRelease>")
        self.text_area.tag_remove("found", "1.0", "end")
        self.text_area.tag_remove("current_found", "1.0", "end")
        self.search_window.destroy()
        self.search_window = None
        self.current_occurrence = 0
        self.search_term = ""

        # Clear the search window reference
        SearchWindow.search_window_instance = None

    def search_text(self, word, direction):
        if not word:
            self.text_area.tag_remove("found", "1.0", "end")
            self.text_area.tag_remove("current_found", "1.0", "end")
            self.occurrences_var.set("")
            return

        # Reset search only if the word changes
        if word != self.search_term:
            self.search_term = word
            self.current_occurrence = 0

        self.text_area.tag_remove("found", "1.0", "end")
        self.text_area.tag_remove("current_found", "1.0", "end")

        occurrences = []
        start_pos = "1.0"

        while True:
            start_pos = self.text_area.search(
                word, start_pos, stopindex="end", nocase=not self.case_sensitive.get()
            )
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(word)}c"
            self.text_area.tag_add("found", start_pos, end_pos)
            occurrences.append(start_pos)
            start_pos = end_pos

        self.text_area.tag_config("found", background="orange")

        count = len(occurrences)
        if count == 0:
            self.occurrences_var.set("No results")
            return

        # Determine current occurrence based on cursor position
        cursor_pos = self.text_area.index("insert")
        for i, pos in enumerate(occurrences):
            if self.text_area.compare(cursor_pos, "<=", pos):
                self.current_occurrence = i if direction == "next" else max(i - 1, 0)
                break
        else:
            self.current_occurrence = count - 1 if direction == "previous" else 0

        if direction == "next":
            self.current_occurrence = (self.current_occurrence) % count
        elif direction == "previous":
            self.current_occurrence = (self.current_occurrence - 1) % count

        # Highlight current occurrence
        if direction in ["next", "previous"]:
            pos = occurrences[self.current_occurrence]
            end_pos = f"{pos}+{len(word)}c"
            self.text_area.tag_add("current_found", pos, end_pos)
            self.text_area.mark_set("insert", end_pos)
            self.text_area.see(pos)
            self.text_area.tag_config("current_found", background="lightgreen")

        # Update label
        self.occurrences_var.set(f"{self.current_occurrence + 1} of {count}")

    def toggle_case_sensitive(self, button, word):
        self.case_sensitive.set(not self.case_sensitive.get())
        self.update_case_sensitive_button(button)
        self.search_text(word, None)

    def update_case_sensitive_button(self, button):
        button.config(fg="blue" if self.case_sensitive.get() else "black")
