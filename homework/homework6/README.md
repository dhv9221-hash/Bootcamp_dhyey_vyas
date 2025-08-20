# Homewrok-6

### Task-1

So for task-1 I imported all the necesarry libraries such as sklearn and seaborn and then created a dataset and saved it in data/raw as raw.csv

### Task-2

in the /src folders I craeted a script called cleaning.py which has 3 functions in oder to normalize the data, filling na with median which means filling in the null values in thcolumn with median value of the column and latly drop na which just drops the rows ith null values


### Task-3

Read the file from data/raw/ and then the price coloumn was a string so I created another coloumn where in i eliminated the '$' sign and converted the string to float

Once done I called missing median function after importing cleaning .py in order to fill a missing sopt in the new float price column with the median of the column.

After this I called the normalize function which used min max scaling in ordr to scaled the data in the range of 0-1 and i put that in a new column in the same dataset called normalized price

Once this was done I called the drop missing function which dropped all the rows woth null vlaues as a result of this the dataset was left with 1 row which was the final processed dataset which I save in data/processed as processed.csv

THe cleaning.py is a resuable file but I assumed that its scope is valid till this task itself hence I have catered it specifically for the dataset I used here
