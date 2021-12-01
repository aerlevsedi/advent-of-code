import pandas as pd

file = open("task3_deliver_input.txt")

line = file.readline()
horizontal = 0
vertical = 0
presents = 0

horizontals = [0]
verticals = [0]

for direction in line :
    
    if direction == '^' :
        horizontal += 1
    elif direction == 'v' :
        horizontal -= 1
    elif direction == '>' :
        vertical += 1
    elif direction == '<' :
        vertical -= 1

    horizontals.append(horizontal)
    verticals.append(vertical)
    
df = pd.DataFrame({'horizontals': horizontals,
                   'verticals': verticals})
  
# print original Dataframe
print(df)
  
# let's Count distinct in Pandas aggregation
df = df.groupby("horizontals").agg({"verticals": pd.Series.nunique})

print(df)
        
print("\n")

print(len(df))