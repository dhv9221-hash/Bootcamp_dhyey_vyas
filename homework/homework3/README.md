# Homework 3

So for this homework I wanted to try it on a different dataset than what was given so I used the iris dataset which is one of the inbuilt datasets in the seaborn library which I installed, importted iris dataset and saved it in data/ as iris.csv

After which I read the dataset by going to data folder and used read_csv function in pandas. After this I called a few basic functions in order to know more about the data set. Functions such as df.head(10) which printedthe first 10 rows of the dataset, df.info which gave me basic info such as data type of each column and whether or not they are non null

I also grouped the data with by category in this case species and saved it in df2
I 

In the src/ folder then i created a utils.py file where in i made a function called data_summary which takes the dataset as the input cals the .describe() fucntion in order to give a small summary of the data and then I saved that summary in data/processed as summary.csv

I then plotted df2 as a bar graph which shows different sepal lenght for different species andI saved it in data/processed as plot.png