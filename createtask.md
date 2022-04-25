{% include nav.html %}

# Create Task

## Runtime
- [Replit Runtime](https://replit.com/@nicm21/CB-Create-Task#main.py)

**Create Task Idea**
-Recommendations for AP classes based on questions

* Did you just receive your CRF for next year? Are you unsure which classes you should take? Can you handle the workload? What APs are easiest? Well, I can help!

* Instructions for input: The Code will use user inputs to search through a list and filter out possibilities

* Use of at least one list (or other collection type): List to store list of AP classes and data for each class (ie. difficulty, prerequisites, etc.)

* Procedure: In order to make my task, I will use a procedure that checks answers to the questions (user generated inputs) and use if functions and other to find what classes work well for the selected inputs

* Algorithm: The algorithm in my program is found in the procedure of my code which uses user generated inputs to select AP classes that work best for the student. It uses Sequencing by running in a specific order, it takes the input and compares it to the classes in the list and then filters out bad options to print or output a filtered list of good AP class suggestions. It uses selection by changing its output based on the decisions and inputs of the user. It uses iteration as it repeats for the number of AP classes needed.

* Calls to your student-developed procedure: After the student selects a submit button to register his response, the procedure to filter the list will be called.

* Instructions for output (tactile, audible, visual, or textual): Based on the program and its use, the output will be textual, displaying the AP Classes that best fit the student.

* Relates to PBL as it gives recommendations for classes in Del Norte

**Video**
* [Video](https://drive.google.com/file/d/1u14zIEh_jV6X8AfYjGW5TGbu8AzW4rF3/view)

**Written Response**
* The overall purpose of the program is to help students narrow down the number of possible AP Classes by giving suggestions based on their input and personality of what AP Classes they should take. With CRF just coming out, it is a helpful tool for students who don't know what classes to take.
* The functionality of the code as demonstrated in the video is imputing information of a student to determine what AP Classes they could take. It takes a few classes from a list of all AP Classes and outputs it to the user.
* The input is the user's response to questions like how many ap's they want to take, what subjects they're interested in, and how hard of an ap they can handle. The output is a few ap classes that they should take and are printed to the user. 
* ![image](https://user-images.githubusercontent.com/89167131/156058267-d356583a-8307-4db5-8553-40f96803db65.png)
* ![image](https://user-images.githubusercontent.com/89167131/156054969-e85575c3-ec0c-42ab-9900-4397bf4caffe.png)
* The name of the list being used in the response is "classes"
* The data contained in the list is all the AP classes offered at Del Norte 
* The list helps sort AP Classes so it can be accessed and taken from based on inputs from the user. It makes it easier than writing out each line with each AP class. Also, the list of Classes is sorted by difficulty so it can output the right AP Classes based on the user's input
* ![image](https://user-images.githubusercontent.com/89167131/156055661-fcc02ba8-4e78-4150-8ccf-f04620f466da.png)
* ![image](https://user-images.githubusercontent.com/89167131/156055731-524d44ac-95e6-4dfd-93f0-df3ac7da7e36.png)
* The procedure makes the code function by taking the user input and determining which outputs or which elements from the list are needed to be outputted. 
* In my algorithm from the procedure, it uses conditionals to output specific elements from a list based on answers or inputs from a user.
* First Call and Second Call: ![image](https://user-images.githubusercontent.com/89167131/156057688-f637f208-7510-4e8d-96af-da05ec3acc6a.png)
* The condition tested of the first call is if the subject they are interested in is science and they can handle a hard AP class, the condition tested of the other call is if the subject they are interested in is social studies and they can handle an easy AP class
* As seen in the above screen shot the output of the first call is difficult science AP classes (Physics 2, Physics C - Mechanics, Physics C - E/M, Chemistry) and the output of the second call is easy social studies AP classes (Human Geography, US Comparative Government, US Gov & Politics)




