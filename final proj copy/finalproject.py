import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

##USEFUL COMMANDS###
#pd.set_option('display.max_rows', None)
#df=pd.read_csv("supermarket_sales.csv", header=0)
#df.drop(["Branch"], axis=1, inplace=True)
#df.drop(["gross margin percentage"], axis=1, inplace=True)
#df.drop(["gross income"], axis=1, inplace=True)
#df.set_index("City", inplace=True)

def duplicates():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)
    #setting branch as the index bc it seems more beneficial to compare the data to the
    #branch rather than the invoice number.

    ilist=[]
    repeats=[]
    for i in df["Invoice ID"]:
        if i in ilist:
            repeats.append(i)
        ilist.append(i)
    print(repeats)
    #there are no repeats of the invoices, so the only thing I can really do with this
    #data is see if the numbers relate to the corresponding product line, so I wont include
    #it in the graphs. This also shows that there are no duplicate rows.
    #there isnt any correlation lol
#duplicates()

def outliers():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)

    #unit price
    plt.boxplot(df["Unit price"], showmeans=True)
    plt.title("Unit Price")
    plt.show()
    #no outliers

    #quantity
    plt.boxplot(df["Quantity"], showmeans=True)
    plt.title("Quantity")
    plt.show()
    #no outliers

    #tax 5%
    plt.boxplot(df["Tax 5%"], showmeans=True)
    plt.title("Tax 5%")
    plt.show()
    #there are outliers, but we aren't removing them because they are valid outliers.

    #cogs
    plt.boxplot(df["cogs"], showmeans=True)
    plt.title("COGS")
    plt.show()
    #there are outliers, but we aren't removing them because they are valid outliers.

    #gross income
    plt.boxplot(df["gross income"], showmeans=True)
    plt.title("Gross Income")
    plt.show()
    #there are outliers, but we aren't removing them because they are valid outliers.

    #rating
    plt.boxplot(df["Rating"], showmeans=True)
    plt.title("Rating")
    plt.show()
    #no outliers

    #total
    plt.boxplot(df["Total"], showmeans=True)
    plt.title("Total")
    plt.show()
    #there are outliers, but we aren't removing them because they are valid outliers.
#outliers()

def extracleaning():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)
    
    #city vs branch
    plt.plot(df.index,df["Branch"])
    plt.xlabel("City")
    plt.ylabel("Branch")
    plt.title("City vs Branch")
    plt.show()
    #after seeing that branch and city literally mean the same thing, I'm going to drop
    #the branch column because city is more descriptive.
    df.drop(["Branch"], axis=1)

    #in addition, simply by scrolling through the data, the gross margin percentage column
    #has the exact same number for every single input, and it doesn't provide any useful
    #information, so I'm also gonna drop it.
    df.drop(["gross margin percentage"], axis=1)

    #it also looked like tax 5% and gross margin had the exact same values, this command
    #proves that it's true, so I'm going to drop the gross income column
    print(df['Tax 5%'].equals(df['gross income']))
    df.drop(["gross income"], axis=1)
#extracleaning()
    
    
    
    

def normalplots():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)

    df.drop(["Branch"], axis=1, inplace=True)
    df.drop(["gross margin percentage"], axis=1, inplace=True)
    df.drop(["gross income"], axis=1, inplace=True)
    df.drop(["Invoice ID"], axis=1, inplace=True)
    

    ######
    #NORMAL PLOTS
    ######

    #all graphs after this point are pretty much redundant, because the simple plots really
    #only measure whether or not each city CONTAINS any of the items in the columns that
    #it's being compared to, which they all do. The data will become more informative
    #once I use graphs that are actually useful.

    #city vs customer type (a bar plot would be easier to read here)
    plt.plot(df.index,df["Customer type"])
    plt.xlabel("City")
    plt.ylabel("Customer type")
    plt.title("City vs Customer type")
    plt.show()

    #city vs gender (a scatter plot would be easier to read here)
    plt.plot(df.index,df["Gender"])
    plt.xlabel("City")
    plt.ylabel("Gender")
    plt.title("City vs Gender")
    plt.show()

    #city vs product line (a scatter plot would be easier to read here)
    plt.plot(df.index,df["Product line"])
    plt.xlabel("City")
    plt.ylabel("Product line")
    plt.title("City vs Product line")
    plt.show()

    #city vs unit price (a scatter plot would be easier to read here)
    plt.plot(df.index,df["Unit price"])
    plt.xlabel("City")
    plt.ylabel("Unit price")
    plt.title("City vs Unit price")
    plt.show()

    #city vs quantity
    plt.plot(df.index,df["Quantity"])
    plt.xlabel("City")
    plt.ylabel("Quantity")
    plt.title("City vs Quantity")
    plt.show()

    #city vs tax 5%
    plt.plot(df.index,df["Tax 5%"])
    plt.xlabel("City")
    plt.ylabel("Tax 5%")
    plt.title("City vs Tax 5%")
    plt.show()

    #city vs total
    plt.plot(df.index,df["Total"])
    plt.xlabel("City")
    plt.ylabel("Total")
    plt.title("City vs Total")
    plt.show()

    #city vs date
    plt.plot(df.index,df["Date"])
    plt.xlabel("City")
    plt.ylabel("Date")
    plt.title("City vs Date")
    plt.show()

    #city vs time
    plt.plot(df.index,df["Time"])
    plt.xlabel("City")
    plt.ylabel("Time")
    plt.title("City vs Time")
    plt.show()

    #city vs payment
    plt.plot(df.index,df["Payment"])
    plt.xlabel("City")
    plt.ylabel("Payment")
    plt.title("City vs Payment")
    plt.show()

    #city vs cogs (cost of good sold)
    plt.plot(df.index,df["cogs"])
    plt.xlabel("City")
    plt.ylabel("Cost of Good Sold")
    plt.title("City vs Cost of Good Sold")
    plt.show()

    #city vs rating
    plt.plot(df.index,df["Rating"])
    plt.xlabel("City")
    plt.ylabel("Rating")
    plt.title("City vs Rating")
    plt.show()
#normalplots()

def histograms():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)

    df.drop(["Branch"], axis=1, inplace=True)
    df.drop(["gross margin percentage"], axis=1, inplace=True)
    df.drop(["gross income"], axis=1, inplace=True)
    df.drop(["Invoice ID"], axis=1, inplace=True)

    nbins=20

    #again, most of this data is virtually useless until I start doing valid comparisons,
    #but it is definitely a lot more useful than the previous graphs.

    
    #unit price
    plt.hist(df["Unit price"],bins=nbins)
    plt.xlabel("Unit Price")
    plt.ylabel("Frequency")
    plt.title("Frequency of Unit Prices")
    plt.show()
    #this shows that there is basically an even amount of prices between all products sold,
    #but there is a spike at ~$98, so there is a good amount of products at that price.

    #quantity
    qbins=10
    plt.hist(df["Quantity"],bins=qbins)
    plt.xlabel("Quantity")
    plt.ylabel("Frequency")
    plt.title("Frequency of Quantities")
    plt.show()
    #after initially plotting this with 20 bins, I saw that there were no rows with quantities
    #above 10, so I changed the amount of bins.
    #this data is very similar to the previous data in the way that everything is virtually equal,
    #until it reaches the max quantity (10), that's where I find the most frequency.

    #tax 5%
    plt.hist(df["Tax 5%"],bins=nbins)
    plt.xlabel("Tax 5%")
    plt.ylabel("Frequency")
    plt.title("Frequency of each 5% Tax Amount")
    plt.show()
    #this data is so so so useless! it has the same purpose as making a histogram
    #of the total price amounts. it just shows the frequency of all tax amounts, which can show
    #the frequency of purchases in different price ranges, but the total amount will already
    #be doing that.

    #total
    plt.hist(df["Total"],bins=nbins)
    plt.xlabel("Total")
    plt.ylabel("Frequency")
    plt.title("Freqnecy of Total Prices Paid")
    plt.show()
    #i explained above, it is exactly the same graph as above, but I do see that most purchases
    #are in the $150 range.

    #cogs
    plt.hist(df["cogs"],bins=nbins)
    plt.xlabel("Cost of Good Sold")
    plt.ylabel("Frequency")
    plt.title("Freqnecy of Cost of Good")
    plt.show()
    #this is also the same graph because it's linear to the prices paid

    #rating
    plt.hist(df["Rating"],bins=nbins)
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.title("Freqnecy of Ratings")
    plt.show()
    
    

    #I originally included date and time in this section, until I realized that pandas didn't
    #detect that I was inputting dates, and was making the histogram not in order of the
    #calendar year, but in the order that it shows up in the file. I'll graph them when I
    #get to the time-series section.

    
    #dbins=12
    #plt.hist(df["Date"],bins=dbins)
    #plt.xlabel("Date")
    #plt.ylabel("Frequency")
    #plt.title("Frequency of Dates")
    #plt.xticks(rotation=90)
    #plt.show()
    #originally I made the bins for this one 365, to see which date had the most amount of purchase,
    #but I learned that I literally could not see the numbers, so I changed the bins to 12 so I could
    #see the month that contained the most amount of purchases. After doing that, and counting to see
    #the bin that had the highest amount of purchases, I learned that it was April, and November had
    #the least.

    #time
    #tbins=24
    #plt.hist(df["Time"],bins=tbins)
    #plt.xlabel("Time")
    #plt.ylabel("Frequency")
    #plt.title("Frequency of Times")
    #plt.xticks(rotation=90)
    #plt.show()    
#histograms()

def timeseries():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.drop(["Branch"], axis=1, inplace=True)
    df.drop(["gross margin percentage"], axis=1, inplace=True)
    df.drop(["gross income"], axis=1, inplace=True)
    df.drop(["Invoice ID"], axis=1, inplace=True)
    df.set_index("City", inplace=True)
    print(df.head())

    df['Date'] = pd.to_datetime(df['Date'])

    #for the timeseries section of this project, im going to make the date the index
    df = df.set_index('Date')

    #going to make columns for each year, month, and day as well to see data for each of those as well
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day'] = df.index.day_name()

    #sort df by date
    df.sort_values(by='Date',inplace=True)
    
    print(df.index.unique().size)
    #this tells me that there are 89 dates, so that;s the amount of binns ill use

    dbins=89
    plt.hist(df.index,bins=dbins)
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.title("Frequency of Dates")
    plt.xticks(rotation=90)
    plt.show()
    #the day with the most amount of purchases was feb 7th

    
    wdbins=7
    plt.hist(df["Day"],bins=dbins)
    plt.xlabel("Day")
    plt.ylabel("Frequency")
    plt.title("Frequency of Days")
    plt.xticks(rotation=90)
    plt.show()
    #the most frequent shopping day was saturday

    mbins=3
    plt.hist(df["Month"],bins=mbins)
    plt.xlabel("Month")
    plt.ylabel("Frequency")
    plt.title("Frequency of Months")
    plt.xticks(rotation=90)
    plt.show()
    #people shopped the most in january

    df=df.set_index('Time')
    df.sort_values(by='Time',inplace=True)
    print(pd.date_range('Time',periods=11))

    tbins=11
    plt.hist((df.index),bins=tbins)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("Frequency of Times")
    plt.xticks(rotation=90)
    plt.show()
    #the most frequent shopping hour is 19:00 (7pm)
        
#timeseries()

def bivariate():
    df=pd.read_csv("supermarket_sales.csv", header=0)
    df.set_index("City", inplace=True)

    df.drop(["Branch"], axis=1, inplace=True)
    df.drop(["gross margin percentage"], axis=1, inplace=True)
    df.drop(["gross income"], axis=1, inplace=True)
    df.drop(["Invoice ID"], axis=1, inplace=True)
    print(df.head())

    pcorr=df.corr()
    print(pcorr)
    print("\n")
    sns.heatmap(pcorr, xticklabels=pcorr.columns, yticklabels=pcorr.columns, cmap="YlGnBu", annot=True, cbar=True)
    plt.show()

    scorr=df.corr(method='spearman')
    print(scorr)
    print("\n")
    sns.heatmap(scorr, xticklabels=pcorr.columns, yticklabels=pcorr.columns, cmap="YlGnBu", annot=True, cbar=True)
    plt.show()


    #CITY
    cvct=pd.crosstab(df.index, df["Customer type"])
    print(cvct)
    print("\n")


    cvg=pd.crosstab(df.index, df["Gender"])
    print(cvg)
    print("\n")

    cvpl=pd.crosstab(df.index, df["Product line"])
    print(cvpl)
    sns.heatmap(cvpl, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print("\n")
    

    cvq=pd.crosstab(df.index, df["Quantity"])
    print(cvq)
    print("\n")

    cvp=pd.crosstab(df.index, df["Payment"])
    print(cvp)
    print("\n")

    cvr=pd.crosstab(df.index, df["Rating"])
    print(cvr)
    sns.heatmap(cvr, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print("\n")
    print("\n")

    #CUSTOMER TYPE
    ctvg=pd.crosstab(df["Customer type"], df["Gender"])
    sns.heatmap(ctvg, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print(ctvg)
    print("\n")

    ctvpl=pd.crosstab(df["Customer type"], df["Product line"])
    print(ctvpl)
    print("\n")

    ctvq=pd.crosstab(df["Customer type"], df["Quantity"])
    print(ctvq)
    print("\n")

    ctvp=pd.crosstab(df["Customer type"], df["Payment"])
    sns.heatmap(ctvp, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    #plt.show()
    print(ctvp)
    print("\n")

    ctvr=pd.crosstab(df["Customer type"], df["Rating"])
    sns.heatmap(ctvr, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    #plt.show()
    print(ctvr)
    print("\n")
    print("\n")

    #GENDER
    gvpl=pd.crosstab(df["Gender"], df["Product line"])
    sns.heatmap(gvpl, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    #plt.show()
    print(gvpl)
    print("\n")

    gvq=pd.crosstab(df["Gender"], df["Quantity"])
    print(gvq)
    print("\n")

    gvp=pd.crosstab(df["Gender"], df["Payment"])
    print(gvp)
    print("\n")

    gvr=pd.crosstab(df["Gender"], df["Rating"])
    sns.heatmap(gvr, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    #plt.show()
    print(gvr)
    print("\n")
    print("\n")

    #PRODUCT LINE
    plvq=pd.crosstab(df["Product line"], df["Quantity"])
    sns.heatmap(plvq, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print(plvq)
    print("\n")

    plvp=pd.crosstab(df["Product line"], df["Payment"])
    print(plvp)
    print("\n")

    plvr=pd.crosstab(df["Product line"], df["Rating"])
    print(plvr)
    print("\n")
    print("\n")

    #QUANTITY
    qvp=pd.crosstab(df["Quantity"], df["Payment"])
    sns.heatmap(qvp, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print(qvp)
    print("\n")

    qvr=pd.crosstab(df["Quantity"], df["Rating"])
    print(qvr)
    print("\n")
    print("\n")

    #PAYMENT
    pvr=pd.crosstab(df["Payment"], df["Rating"])
    sns.heatmap(pvr, cmap="YlGnBu", annot=True, cbar=True, fmt='g')
    plt.show()
    print(pvr)
    print("\n")
    print("\n")

    #product line v total
    plvt=df.pivot_table(index=["Product line"], values=["Total"], aggfunc=[np.sum, np.mean])
    print(plvt)
    print("\n")

    #mean money spent per gender
    gvt=df.pivot_table(index=["Gender"], values=["Total"], aggfunc=[np.sum, np.mean])
    print(gvt)
    print("\n")

    #money per customer type
    ctvt=df.pivot_table(index=["Customer type"], values=["Total"], aggfunc=[np.sum, np.mean])
    print(ctvt)
    print("\n")

    #money per payment type
    ptvt=df.pivot_table(index=["Payment"], values=["Total"], aggfunc=[np.sum, np.mean])
    print(ptvt)
    print("\n")

    #rating per gender
    rvg=df.pivot_table(index=["Gender"], values=["Rating"], aggfunc=np.mean)
    print(rvg)
    print("\n")

    #customer type v rating
    rvct=df.pivot_table(index=["Customer type"], values=["Rating"], aggfunc=np.mean)
    print(rvct)

    
   
bivariate()

    
    
    


    
