# hoohacks2023
## Inspiration
Every day, minor occurrences such as unused and plugged outlets, inefficient insulation, and dirty refrigerator coils lead to energy waste-- each year wasting millions of dollars and an abundance of resources. From large universities to small households, everyone can increase their energy efficiency, lower their power consumption, and leave a smaller footprint on today's already vulnerable environment. 

## What it does
Our website takes user responses about the daily use of everyday electronics and returns the user suggestions on how to lower their power usage. Our responses are personalized as the backend program detects the severity of electricity waste based on each question(the specific appliance we are asking for)

## How we built it
HTML, CSS make up our text, messages to the user, and basic aesthetic to our website. Javascript is mainly used to store variables in to localstorage, and finally save data into a .txt file(however javascript is also used for some animations in our buttons). Finally, python is used purely in for our back-end; it takes data from the javascript generated text file, analyzes that data, and generates a 2nd .txt file for javascript to read, and display for the user.
## Challenges we ran into
While the project works and gives us accurate results, it is not user friendly. If released right now, after submitting the survey, the user would have to run a python file that reads and writes a text file based on input data by him/herself. In short, functional websites generate feedback/results with the click of a button, while ours needs multiple "button clicks" and wont complete if the user doesn't run a python program.

## Accomplishments that we're proud of
While using our webapp is a little comlex for our users, we were technically able to connect our front and back ends together, meaning our site is technically fully functional. 

## What we learned
During the hackathon, we learned the different components of a website(front and back end), and we now know how to use our previous knowledge in programming to code both ends, and somewhat connect them. 

##Whats next
Most websites with offer functionality and expirence large traffic are hosted through the cloud, use APIs to transition from front end and back end, etc. If we want to achieve a similar structure with our project, all three of us would need to learn the basics of hosting websites on the cloud, hosting/running servers, using react, etc.

## What's next for Powr
1. Functionality: Make sure the user can get results in a timely manner with the click of one button
2. Determine and work on a more specific algorithm, to give the user even better results
3. Do more research on what causes energy waste and the solutions to those problems
4. Re-route users to useful sites based on their response, whether it is a service or a blog post
