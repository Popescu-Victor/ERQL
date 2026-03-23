def enter(): # Just proof of concept for the time being. Later on I'll replace the many if-statements below with a hashmap.
    user_input = entry.get()
    rendered = interpreter.Render(user_input)
    if rendered.subj == "standard":
        if rendered.verb == "plot":
            fig = erql.scatter_plot(rendered.mod[0], rendered.mod[1])
            print('returned fig')
            canvas_widget = FigureCanvasTkAgg(fig, master=canvas1)
            canvas_widget.draw()
            canvas_widget.get_tk_widget().pack(fill="both", expand=True)
            
        if rendered.verb == "clear":
            text_box.delete('1.0', tk.END)
            
        if rendered.verb == "upload":
            uploaded_file = erql.upload()
            file_info = f"Column Names: \n *************** \n {uploaded_file.file.columns.tolist()}"
            text_box.insert(tk.END, file_info)
                if rendered.subj == "file":
                    
        if rendered.verb == "plot":
            for widget in canvas1.winfo_children():
                widget.destroy()
            fig = erql.scatter_file(rendered.mod[0], rendered.mod[1])
            canvas_widget = FigureCanvasTkAgg(fig, master=canvas1)
            canvas_widget.draw()
            canvas_widget.get_tk_widget().pack(fill="both", expand=True)

    if rendered.subj == "groups":
        if rendered.verb == "display":
            conn = sqlite3.connect("db.sqlite")
            cursor = conn.cursor()
            for row in cursor.execute("SELECT * FROM users"):
                text_box.insert(tk.END, row)
