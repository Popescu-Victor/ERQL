# help> This is the basic 'help' command that gives instructions for first time users.
help_text = ("""

Welcome to ERQL! Here's a brief overview of how this program works:

Unlike other reporting software like Excel and PowerBI, ERQL works entirely based on simple scripts. \n\n

Here's an example of a basic script you can try: \n 
file>upload>csv \n

There are three parts in this command, which are conveniently named after parts of speech. There's a subject (file), a verb (upload) and an object (csv). This command tells the program you wish to:
\n 1. Have a file perform an action.
\n 2. Have that action be an upload (of itself in this case)
\n 3. Have the type of file be .csv.

\n\n Although ERQL can work with Excel files as well, to avoid formatting errors caused by using different versions we strongly recommend saving your files in .csv before working on them.
\n\n Enter "help>" + one of the following 'verbs' to get more information:
\n\n graph - for creating graphs and charts
\n file - for storing .csv files in the program's memory
\n homework - for parsing through homework data
\n virtual_class - for parsing through vc data
\n save - for saving the graph or the text into a separate file
\n group - for matching students to their tutor and storing these relations in a database

             """)

help_fun = { "file>upload":"Stores a file in memory and returns some basic information about it in order to aid future analysis.\n\n"
}

# help>homework
help_homework = "Upload a file using 'file>upload' then convert the raw scrapped excel file into ILIAS code using 'homework>convert'"

# help>graph
help_graph = "Upload a file using file>upload and then do the following: \n\n" \
"Pick the type of graph you want to have displayed: \n 1. 'bar' for bar chart \n 2. 'scatter' for scatter plot \n 3. 'correlation' for scatter plot with trendline \n\n Finally, pick the two columns with data that you wish to have displayed and add them to the script. In the end you should have something like this: \n graph>bar>hours_spent_studying>final_grade"

# help>file
help_file = "The file verb is used to store .csv files in the program's memory. To upload a file, use the following script: \n\n file>upload>csv \n\n where 'csv' is the type of file you wish to upload. You can also use 'excel' if you wish to upload an excel file, but we recommend converting it to .csv first to avoid formatting errors."

# help>virtual_class
help_virtual_class = "Upload a file using 'file>upload' then convert the raw scrapped csv file into ILIAS code using 'virtual_class>convert'. Paste the resulting code into the ILIAS page to have it displayed as a table with links to each unscorred assignment."

# help>save
help_save = "After creating a graph or parsing through some data, you can save the resulting graph or text into a separate file using the 'save' verb. To do this, use the following script: \n\n save>graph>png \n\n where 'graph' is the type of content you wish to save and 'png' is the type of file you wish to save it as. You can also use 'text' instead of 'graph' if you wish to save some text instead of a graph."

def stats_hist(file):
    text = f"Successfully created histograms for '{file}'. \nThe dotted red line marks the median."
    return text