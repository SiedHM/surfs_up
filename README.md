# Challenge-9
By: Sied H. Mohamed

# Purpose of the project
The purpose of this project is to generate descriptive analysis of temperature months of June and December in Oahu, in order to determine if opening surf and ice cream shop business is sustainable year-round.

# Data source and method
I used a SQLite data, “hawaii.sqlite” , provided by the bootcamp is used for the analyses. SQLite databases are flat files, which means that they don't have relationships that connect the data to anything else. As a result, flat files can be stored locally, which will help us move more quickly through the analysis.

SQLAlchemy libray is used to analyses the temperature using python in Jupyter    notebook platform. In addition to SQLAlchemy, I also used pandas library.


# Results.
Evidences show that the demand and sale of ice cream and surfing service depend on weather.  It is expected that the demand and sale to be higher with the hotter the temperatures. Tables 1 and 2 below shows that the average temperature in the month of June is about 75 while for December it is about 71. There is only 4-degree Fahrenheit difference in the average temperature of the two months. Further, the interquartile range (IQR) for the month of June is about 4 and for December is about 5. The similarity in both mean temperature and IQR implies that the weather is sustainable and suitable for opening ice cream shop.

 #### Table-1: Descriptive statistics for the month of June
 
![Table-1](https://github.com/nebil2016/surfs_up/blob/main/Resources/June%20temprature.png)

##### Table-2: Descriptive statistics for the month of December

![Table-2](https://github.com/nebil2016/surfs_up/blob/main/Resources/December%20temp.png)

# Conclusion.
The similarity of the temperatures in the months of June and December in terms of mean and interquartile rage implies that temperature is suitable and sustainable for ice-cream business.  The mean temperatures in both months indicate a hotter temperature and this is an ideal temperature for a higher demand of cream and surfing. 

