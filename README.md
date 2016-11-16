# Lyft4Humanity

### Help the homeless.
### Version 1.0

#### How to run this project:
```
  git clone https://github.com/Hive-Labs/Wingman
  cd Wingman    
  npm install
  npm start or node app.js
```

#### Technology

    - [Express.js](http://expressjs.com/) - Framework used to build the REST-based backend.
    - [Node.js](https://nodejs.org/en/) - Evented I/O for the backend.
    - [jQuery](https://jquery.com/) - Make life easy.
    - [Bootstrap](http://getbootstrap.com/) - Template.
    - 3rd party API: Typeform Data API.

###### Output:
    - Lyft code

#Inspiration
"I didn't realize how big the homeless problem was here."

"I saw a man outside of the food store, begging for change so he could catch a ride home. Later, I was in a Lyft, and I jokingly asked the driver how she would feel about driving homeless people around, and she said she wouldn't mind it. I mean they can't pay for their own rides. So I was like, you know, why not crowdfund it?" -Tony

Oftentimes, people find themselves in situations where their burden could be eased if they just had a means of transportation: jobs, hospitals, distant family; people miss out on opportunities by not having transportation, and by crowdfunding a way for them to get around, we can help with commutes, relocation, and so much more. Together it can all come together to help a person get back on their feet.

#What it does
Lyft4Humanity is a web application designed to assist homeless shelters in getting people back on their feet. It acts as a database for shelters to keep track of and more efficiently assist the displaced as they get back on their feet. More importantly, it connects to the community, providing them with an opportunity to play a role in making the community a better place. Lyft4Humanity acts as a crowdfunding application, aimed specifically at bringing beneficiaries an often overlooked but essential tool, transportation. This way, shelters can provide members with access to resources, which in turn can lead to an opportunity to get a new start.

#How we built it
The back-end of Lyft4Humanity is written in Python. The database is powered by MongoDB, running off of a Linode Ubuntu server. The Lyft API handles rides, while Nessie simulates payments and transactions between contributors and accounts. It utilizes Flask to connect the back-end to the front-end, which is written using HTML, CSS, and JS, built on Node.js and utilizing the Typeform API for form filling. Nexmo is used for voice and SMS notifications to keep everyone involved in the loop.

#Challenges we ran into
One of our biggest challenges was connecting the front-end to back-end in different languages (Python and JS). There was also a gap in experience between members of the team, so finding a way to merge different coding practices further exaggerated such issues. We also ran into problems running MongoDB on our own computers, most likely because of the school's firewall, and we used Linode as a solution. Another common issue was incorporating APIs into Python. For example, Lyft's API presented many issues with HTTP requests that were difficult to transfer into Python. Typeform proved to be another challenge to work with in Python when it returned malformed, difficult to fix JSON collections. Retrieving data from MongoDB with Typeform also proved difficult. Overall, although we ran into some hurdles, each of these challenges was eventually overcome in the completed proof of concept.

#Accomplishments that we're proud of
Learning a noSQL database like MongoDB was an interesting and challenging experience. The Typeform integration with the UI came out very nice. Learning so many new tools and APIs in such a short time was challenging but rewarding.

#What we learned
We each learned a lot about new tools, and along with that some self teaching that will come in handy when learning new technologies in the future. We also discovered a rewarding twist on a previously existing idea and used to it to create something that can benefit others.

#What's next for Lyft4Humanity
As with any application that handles money and personal data, security is a major issue that needs to be addressed. Lyft4Humanity is not an insecure app, but security is something that should have a closer look taken at as it is further developed. Expanded database functionality would also be great; right now there is a wealth of unused data being stored. With the use of this data would naturally come new features, such as a "where are they now" that could allow people to see the progress of the people they have aided. Alongside this could come meetings or connections between users of Lyft4Humanity, and it is our hope that in this way communities will nurture their people and become closer.
