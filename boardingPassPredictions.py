'''
File Name:
Description:
Author: Cathal Brolly
Edited on: 27/09/2021
'''

from sklearn import tree
import sys

def predictingDestination():
    age = input("What age are you?\n")
#validAge(age, discount)
#age = input("What age are you?\n")
    if age.isdigit() == False:
        print("That's not an age!")
        age = input("What age are you?\n")

    if int(age) >= 65:
        discount = "20%"
    elif int(age) < 18:
        print("You cannot fly!")
        discount = "0%"
        sys.exit()
    else:
        discount = "0%"

    travelData = [[22, "Madrid"], [33, "London"], [29, "London"], [27, "London"],
              [45, "Paris"], [55, "Paris"], [19, "Madrid"], [65, "Belfast"],
              [48, "Paris"], [28, "Madrid"], [58, "Belfast"], [31, "London"],
              [38, "Paris"], [24, "Madrid"], [69, "Belfast"], [35, "London"]]

    travelAge = [x[0] for x in travelData]

    destination = [x[1] for x in travelData]

    model = tree.DecisionTreeClassifier()


# What is happening here?

    for item in travelData:
        item.pop()

    model.fit(travelData, destination)

    prediction = model.predict([[age]])

    print(f"You should fly to {prediction}")

predictingDestination()

#import graphviz
# DOT data
#dot_data = tree.export_graphviz(model, out_file=None,
                                #feature_names=["height", "weight","shoe"],
                                #class_names=["male", "female"],
                                #filled=True)

# Draw graph
#graph = graphviz.Source(dot_data, format="png")
#graph
#graph.render("decision_tree_graphivz")
