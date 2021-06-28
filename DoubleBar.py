from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

#function to generate x values, this makes sure they are side by side along the graph.

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

#matplotlib automatically uses 0.8 spacing hence the 0.8 in the lists declared below
#the first parameter is the number of dataframes we are comparing,second is the spacing,third is the dataframe we are on, and lastly is how many bars there is.
school_a_x = create_x(2,0.8,1,5) 
school_b_x = create_x(2,0.8,2,5)

plt.figure(figsize=(10,8))
ax = plt.subplot()
plt.bar(school_a_x,middle_school_a)
plt.bar(school_b_x,middle_school_b)

#creating the x coordinates list to be inbetween the two sets of data we have.
middle_x = [(a+b)/2 for (a,b) in zip(school_a_x,school_b_x)]

ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend(['Middle School A','Middle School B'])
plt.xlabel('Unit')
plt.ylabel('Test Average')
plt.title('Test Averages on different units')
plt.show()


plt.savefig('my_side_by_side.png')
