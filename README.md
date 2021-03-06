# Food Ratings

Machine learning approaches to predicting and classifying food ratings

## Dataset

Data used will be from [here](http://snap.stanford.edu/data/web-FineFoods.html)
Which consists of over 500k reviews aggregated from Amazon between
Oct 1999 - Oct 2012.

Example format of one review:

```
product/productId: B001E4KFG0
review/userId: A3SGXH7AUHU8GW
review/profileName: delmartian
review/helpfulness: 1/1
review/score: 5.0
review/time: 1303862400
review/summary: Good Quality Dog Food
review/text: I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than most.
```

## Formatting data

Since the dataset given is in a flat text file there is a python script that
transforms the data into CSV format. Each review is placed into one row of
the CSV and only the values of each field are placed in the columns.

To run against the original dataset pass the path to the file

`python formatdata.py ~/Path/To/finefoods.txt`

And this will output `finefoods.csv` with the first 5 lines looking like:

```
"B001E4KFG0","A3SGXH7AUHU8GW","delmartian",1.0,5.0,1303862400,"Good Quality Dog Food","I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than  most."
"B00813GRG4","A1D87F6ZCVE5NK","dll pa",0.0,1.0,1346976000,"Not as Advertised","Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as ""Jumbo""."
"B000LQOCH0","ABXLMWJIXXAIN","Natalia Corres ""Natalia Corres""",1.0,4.0,1219017600,"""Delight"" says it all","This is a confection that has been around a few centuries.  It is a light, pillowy citrus gelatin with nuts - in this case Filberts. And it is cut into tiny squares and then liberally coated with powdered sugar.  And it is a tiny mouthful of heaven.  Not too chewy, and very flavorful.  I highly recommend this yummy treat.  If you are familiar with the story of C.S. Lewis' ""The Lion, The Witch, and The Wardrobe"" - this is the treat that seduces Edmund into selling out his Brother and Sisters to the Witch."
"B000UA0QIQ","A395BORC6FGVXV","Karl",1.0,2.0,1307923200,"Cough Medicine","If you are looking for the secret ingredient in Robitussin I believe I have found it.  I got this in addition to the Root Beer Extract I ordered (which was good) and made some cherry soda.  The flavor is very medicinal."
"B006K2ZZ7K","A1UQRSCLF8GW1T","Michael D. Bigham ""M. Wassir""",0.0,5.0,1350777600,"Great taffy","Great taffy at a great price.  There was a wide assortment of yummy taffy.  Delivery was very quick.  If your a taffy lover, this is a deal."
```
