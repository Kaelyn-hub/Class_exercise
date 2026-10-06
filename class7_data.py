import pandas as pd
data = {"ID":range(100),"Score":[10]*2+[20]*3+[30]*5+[50]*15+[60]*20+[70]*25+[80]*15 +[90]*8 +[100,100,5,5,0,0,5000]}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)
print(df.shape)
print(df.describe())
'''
print(df.shape)
print(df.dtypes)
print(df.describe())

df_original = df.copy()

import matplotlib.pyplot as plt
df['Score'].plot.hist(bins=300, edgecolor='black')
plt.show()

#Without the last score of 5000. 
df['Score'][:-1].plot.hist(bins=300, edgecolor='black')
plt.show()

# IQR
'''
q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1

# Use the equation above to replace None
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(lower)
print(upper)

df_score_cleaned = df[(df["Score"] >= lower) & (df["Score"] <= upper)]

#Z-SCORE
mean = df["Score"].mean()
std = df["Score"].std()

z_scores = (df["Score"] - mean) / std
print(z_scores)

df_score_cleaned = df[z_scores.abs() <= 3]
print(df_score_cleaned)
'''
import pandas as pd
data = {"ID":range(4),"Message":["Now Here  "," now here ", "  NOW HERE", "Now   here"]}
df = pd.DataFrame(data)
print(df)

df["Message"] = df["Message"].str.strip()
print(df)
# Convert to Lowercase
df["Message"] = df["Message"].str.lower() 
print(df)

# removing repeated whitespace between words?
print(df["Message"].str.replace(' ',''))
'''



'''
import re
print(re.sub(r"\s+", " ", "Hi     there"))

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

df["Message"] = df["Message"].apply(clean_text)

links = ["Visit https://example.com for more info", "My link: www.github.com/mylink/", "Visit http://www.google.com/search"]
data = pd.Series(links)

print(data)

def replace_url(text):
    text = re.sub(r"https?://\S+|www\.\S+", "URL", text)
    return text
# Remove URLs
data = data.apply(replace_url)
print(data)

'''