def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()  # Sort intervals based on the start time
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        
        if start <= last_end:
            merged[-1][1] = max(last_end, end)  # Merge overlapping intervals
        else:
            merged.append([start, end])  # Add non-overlapping interval
    
    return merged

# Example usage
intervals = [[1,3],[2,4],[5,6],[8,10]]
result = merge_intervals(intervals)
print(result)  # Output: [[1, 4], [5, 6], [8, 10]]




def filter_value(users):
    result = {}

    for user in users:
        profile = user.get("profile", {})
        if user.get("active") and "city" in profile:
            city = profile["city"].lower()
            name = profile["name"].lower()

            if city not in result:
                result[city] = []

            result[city].append(name)

    return result

users = [
    {"profile": {"name": "Tushar", "email": "tushar@datahash.com", "city": "bangalore"}, "active": True},
    {"profile": {"name": "Sachin", "email": "sachin@datahash.com", "city": "bangalore"}, "active": True},
    {"profile": {"name": "Rahul", "email": "rahul@datahash.com", "city": "gurgaon"}, "active": False},
    {"profile": {"name": "Sid", "email": "sid@datahash.com", "city": "gurgaon"}, "active": True},
    {"profile": {"name": "John", "email": "john@datahash.com"}, "active": True}
]

output = filter_value(users)
print(output)

#output
{"bangalore": ["tushar", "sachin"], "gurgaon": ["sid"]}

Used user.get("profile", {}) to avoid errors if profile is missing.
Lowercased city and name for consistency.
Ensured city exists before using it.


Here is the Django model definition for the given query:
    
from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ve_name

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annualvesseleanalysis")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.year}"
        


This model structure ensures:

A one-to-many relationship between Vessele and AnnualVesseleAnalysis using a foreign key.
The fields plaenty and year in AnnualVesseleAnalysis are nullable, matching the query conditions.


Primary Keys:
Vessele Model:

vesseled_id is the primary key (AutoField, meaning it auto-increments).
AnnualVesseleAnalysis Model:

By default, Django provides an implicit primary key called id (since no explicit primary key is defined).
The id field is automatically created as an AutoField unless you explicitly define a different primary key.

Foreign Key:
AnnualVesseleAnalysis Model:
The vessele field in AnnualVesseleAnalysis is a foreign key that references Vessele.vesseled_id.
on_delete=models.CASCADE ensures that when a Vessele is deleted, its related AnnualVesseleAnalysis records will also be deleted.


Summary:
Primary Key:
vesseled_id in Vessele
id (default) in AnnualVesseleAnalysis
Foreign Key:
vessele in AnnualVesseleAnalysis (references Vessele.vesseled_id)


1. Explanation of the Django Query
The given Django query is written using Django's ORM (Object-Relational Mapping) to filter and retrieve data from a database. Let’s break it down step by step.

from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ve_name

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annualvesseleanalysis")
    plaenty = models.CharField(max_length=255, null=True, blank=True)  # Can be NULL
    year = models.IntegerField(null=True, blank=True)  # Can be NULL

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.year}"


Vessele Model: Represents vessels with a unique vesseled_id (Primary Key).
AnnualVesseleAnalysis Model: Represents an annual analysis of a vessel. It has a ForeignKey (vessele) referencing Vessele.
plaenty and year fields are allowed to be NULL (null=True, blank=True).
on_delete=models.CASCADE ensures that if a Vessele is deleted, its related AnnualVesseleAnalysis records will also be deleted.



2. Understanding the Query


from django.db.models import Q
from your_app.models import Vessele, AnnualVesseleAnalysis

# Query to join Vessele with AnnualVesseleAnalysis where plaenty and year are NULL
result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
).values(
    'vesseled_id', 've_name', 'annualvesseleanalysis__plaenty', 'annualvesseleanalysis__year'
)


Breakdown of the Query
Vessele.objects.filter(...)

This is a Django ORM query that filters the Vessele table.
It applies conditions on related AnnualVesseleAnalysis records.
annualvesseleanalysis__plaenty__isnull=True

This checks if the plaenty field in AnnualVesseleAnalysis is NULL.
annualvesseleanalysis__year__isnull=True

This checks if the year field in AnnualVesseleAnalysis is NULL.
values(...)

This method retrieves only specific fields instead of returning full model instances.
Fields retrieved:
vesseled_id (Primary Key of Vessele)
ve_name (Vessel name)
annualvesseleanalysis__plaenty (Penalty field, expected to be NULL)
annualvesseleanalysis__year (Year field, expected to be NULL)


3. How the Query Works

Join Between Tables:

The filter conditions are on AnnualVesseleAnalysis, but we are querying from Vessele.
Django ORM automatically performs an INNER JOIN between Vessele and AnnualVesseleAnalysis using the ForeignKey (vessele).
Filtering Records:

The query selects only Vessele records where at least one related AnnualVesseleAnalysis record has both plaenty and year as NULL.
Returning Data as a Dictionary:

.values(...) ensures the result is a list of dictionaries, not model instances.

4. Output of the Query

The final result is iterated and printed:
# Output the result
for row in result:
    print(row)


Example Data in Database
vesseled_id	ve_name	plaenty	year
1	Ship A	NULL	NULL
2	Ship B	Fine	2023
3	Ship C	NULL	NULL

Result of the Query
{'vesseled_id': 1, 've_name': 'Ship A', 'annualvesseleanalysis__plaenty': None, 'annualvesseleanalysis__year': None}
{'vesseled_id': 3, 've_name': 'Ship C', 'annualvesseleanalysis__plaenty': None, 'annualvesseleanalysis__year': None}

Only Ship A and Ship C are included since their plaenty and year are NULL.

5. SQL Equivalent Query
The Django ORM query is translated into the following SQL query:

SELECT v.vesseled_id, v.ve_name, a.plaenty, a.year
FROM Vessele v
JOIN AnnualVesseleAnalysis a ON v.vesseled_id = a.vessele_id
WHERE a.plaenty IS NULL AND a.year IS NULL;


6. Key Takeaways
Django ORM automatically performs a JOIN between Vessele and AnnualVesseleAnalysis.
isnull=True filters NULL values in plaenty and year.
Only vessels having at least one related record with plaenty and year as NULL are retrieved.
.values(...) returns a dictionary-like structure, not model instances.
The query is equivalent to an SQL INNER JOIN with a WHERE condition.


✅ Alternative Approaches

If you want all Vessele records, even those without related AnnualVesseleAnalysis entries, use outerjoin:

result = Vessele.objects.filter(
    Q(annualvesseleanalysis__plaenty__isnull=True) & 
    Q(annualvesseleanalysis__year__isnull=True)
).values('vesseled_id', 've_name')


This ensures even vessels without any AnnualVesseleAnalysis entries are included.


To avoid duplicate vessel records, use distinct():

result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
).values('vesseled_id', 've_name').distinct()


This Django query is an efficient way to filter related data. Understanding how Django ORM translates to SQL is crucial for optimizing performance in large databases.


***How is annualvesseleanalysis Name Decided in the Query?
In the Django ORM query:

result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
)


The name annualvesseleanalysis is automatically generated by Django based on the related_name of the ForeignKey in the AnnualVesseleAnalysis model.


How Django Determines the Related Name
1. Checking the ForeignKey Definition
Let's look at the model definition:


class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annualvesseleanalysis")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)



The ForeignKey field is vessele, which establishes a relationship between AnnualVesseleAnalysis and Vessele.
The parameter related_name="annualvesseleanalysis" explicitly defines the reverse relation name.
Since related_name="annualvesseleanalysis" is provided, Django uses this name for queries on the Vessele model.


2. What if related_name is Not Defined?
If we didn't specify related_name, Django would automatically generate a name based on the model name in lowercase + _set.

For example:

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE)  # No related_name

Django would automatically assign the reverse relation name as:
    Vessele.annualvesseleanalysis_set


Thus, the query would change to:
result = Vessele.objects.filter(
    annualvesseleanalysis_set__plaenty__isnull=True,
    annualvesseleanalysis_set__year__isnull=True
)



Key Takeaways:
    
The name annualvesseleanalysis in the query comes from the related_name="annualvesseleanalysis" defined in the ForeignKey.
If no related_name is provided, Django defaults to <model_name>_set (e.g., annualvesseleanalysis_set).
This related name allows reverse access from Vessele to its related AnnualVesseleAnalysis records.


1. First Query (Direct Filtering)

result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
).values(
    'vesseled_id', 've_name', 'annualvesseleanalysis__plaenty', 'annualvesseleanalysis__year'
)


Key Characteristics:
✅ Implicit AND Condition:

The conditions are passed as keyword arguments.
Django automatically combines them using AND (plaenty IS NULL AND year IS NULL).
✅ Cleaner Syntax:

Directly filtering without explicitly using Q().
✅ Includes plaenty and year in .values(...):

The result will contain:
vesseled_id
ve_name
annualvesseleanalysis__plaenty
annualvesseleanalysis__year


2. Second Query (Using Q Objects for Filtering)

result = Vessele.objects.filter(
    Q(annualvesseleanalysis__plaenty__isnull=True) & 
    Q(annualvesseleanalysis__year__isnull=True)
).values('vesseled_id', 've_name')


Key Characteristics:
✅ Explicit AND Condition (&) with Q Objects:

The & operator explicitly combines conditions as AND.
This is more flexible if we later need OR (|) conditions.
✅ More Readable for Complex Queries:

If filtering conditions were more complicated (e.g., multiple OR conditions), using Q objects would be clearer.
✅ Excludes plaenty and year in .values(...):

Only vesseled_id and ve_name are included in the result.
This means the output does not return plaenty and year in the dictionary.


Summary: When to Use Which?
Feature	First Query (Direct)	                         Second Query (Q Object)
Syntax	Simpler, direct filtering	                      More explicit and flexible
Condition Joining	Implicit AND	                     Explicit AND (&)
Use Case	When filtering with AND conditions only	     When mixing AND/OR conditions
Readability	Easier for simple conditions	             Better for complex conditions
Result Fields	Includes plaenty and year	              Excludes plaenty and year


 When to Use Q?
Use Q objects when:

1)You need OR conditions (|).

result = Vessele.objects.filter(
    Q(annualvesseleanalysis__plaenty__isnull=True) | 
    Q(annualvesseleanalysis__year__isnull=True)
)

This will match records where either plaenty or year is NULL.

2)You have complex nested conditions.
result = Vessele.objects.filter(
    Q(annualvesseleanalysis__plaenty__isnull=True) & 
    (Q(annualvesseleanalysis__year__isnull=True) | Q(ve_name="Titanic"))
)


This selects vessels where:

plaenty is NULL AND
(year is NULL OR ve_name is "Titanic")


📌 Final Recommendation
✅ For simple AND conditions: Use the first query.
✅ For complex conditions (AND/OR mixing): Use Q() for better readability and flexibility.



Understanding Different Relationship Queries in Django ORM
Django provides three main types of database relationships:

One-to-Many (ForeignKey)
One-to-One (OneToOneField)
Many-to-Many (ManyToManyField)


1️⃣ One-to-Many Relationship (ForeignKey)


class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_analyses")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)



Query Explanation
Query 1: Filtering using implicit AND


result = Vessele.objects.filter(
    annual_analyses__plaenty__isnull=True,
    annual_analyses__year__isnull=True
)


This filters Vessele records having at least one related AnnualVesseleAnalysis where both plaenty and year are NULL.
annual_analyses is the reverse relation name due to related_name="annual_analyses"


Query 2: Using Q() objects

result = Vessele.objects.filter(
    Q(annual_analyses__plaenty__isnull=True) & 
    Q(annual_analyses__year__isnull=True)
)


Uses Q objects to explicitly apply the AND condition.
More useful when combining with OR (|) conditions.

2️⃣ One-to-One Relationship (OneToOneField)

class VesseleDetails(models.Model):
    vessele = models.OneToOneField(Vessele, on_delete=models.CASCADE, related_name="details")
    manufacturer = models.CharField(max_length=255)
    build_year = models.IntegerField()

Query Explanation

Query 1: Filtering with Direct Access
result = Vessele.objects.filter(details__manufacturer="ABC Corp")


Directly accesses the related VesseleDetails using related_name="details".
Finds vessels where manufacturer is "ABC Corp".



Query 2: Using Q() for Complex Conditions
result = Vessele.objects.filter(
    Q(details__manufacturer="ABC Corp") & 
    Q(details__build_year__gte=2000)
)


Finds vessels where manufacturer is "ABC Corp" AND build year is ≥ 2000.

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)  # Accessing OneToOneField


Query 3: Accessing Related Data

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)  # Accessing OneToOneField


Fetches VesseleDetails using .details (reverse relation).


3️⃣ Many-to-Many Relationship (ManyToManyField)

class CrewMember(models.Model):
    name = models.CharField(max_length=255)

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    crew = models.ManyToManyField(CrewMember, related_name="vesseles")


Query Explanation
Query 1: Filtering Vessels by Crew Member

result = Vessele.objects.filter(crew__name="John Doe")


Finds all vessels where at least one crew member is named "John Doe".




✅ Optimized Query Using prefetch_related
If you’re going to access the related crew members after retrieving the vessels, you should use prefetch_related() to avoid N+1 query problems.


vessels = Vessele.objects.prefetch_related('crew').filter(crew__name="John Doe")

💬 Meaning:
"Get all vessels that have a crew member named 'John Doe', and efficiently prefetch all crew members for each vessel."

🧠 Why use prefetch_related?
Without it:

Django will run 1 query to get the vessels.

Then run 1 separate query per vessel to get its crew.

With it:

Django runs only 2 queries total, no matter how many vessels are returned.


🛟 Bonus: Display All Crew Names Per Vessel
for vessel in vessels:
    print(f"Vessel: {vessel.ve_name}")
    for crew_member in vessel.crew.all():
        print(f" - Crew: {crew_member.name}")


Perfect! Let's now cover the reverse query — where you want to find crew members assigned to a specific vessel, either by its name or ID.


✅  Get All Crew Members of a Vessel by ID
Assuming you have the vessel ID (e.g., from a request or URL):
    
    
🔍 Query:
 vessel = Vessele.objects.get(vesseled_id=1)
crew_members = vessel.crew.all()


💬 Meaning:
“Get the vessel with ID = 1, then fetch all its assigned crew members.”

✅  Get All Crew Members of a Vessel by Name
vessel = Vessele.objects.get(ve_name="Ocean Spirit")
crew_members = vessel.crew.all()


“Get the vessel named 'Ocean Spirit' and retrieve its crew members.”


✅ 3. Use Related Name to Go from CrewMember Side
Since you defined the ManyToManyField in Vessele with:

crew = models.ManyToManyField(CrewMember, related_name="vesseles")


You can also do the reverse lookup from the CrewMember side:

crew_member = CrewMember.objects.get(name="John Doe")
vessels = crew_member.vesseles.all()


“Get all vessels that crew member 'John Doe' is assigned to.”

✅ The .vesseles part comes from related_name="vesseles".


🧠 Best Practice Tip
To avoid multiple DB hits in templates or APIs:
    
    
 crew_members = CrewMember.objects.prefetch_related('vesseles').all()


or

vessel = Vessele.objects.prefetch_related('crew').get(ve_name="Ocean Spirit")

    
    
    
    


  


Query 2: Using Q() for Complex Filters

result = Vessele.objects.filter(
    Q(crew__name="John Doe") | Q(crew__name="Jane Doe")
)


Finds vessels where at least one crew member is either "John Doe" OR "Jane Doe".


Query 3: Fetching Crew Members for a Vessel
vessel = Vessele.objects.get(vesseled_id=1)
crew_members = vessel.crew.all()


Retrieves all crew members associated with the vessel.

📌 Summary of Queries
Relationship Type	Query Type	Example Query
One-to-Many (ForeignKey)	Filtering	Vessele.objects.filter(annual_analyses__plaenty__isnull=True)
Q() Filtering	Vessele.objects.filter(Q(annual_analyses__plaenty__isnull=True) & Q(annual_analyses__year__isnull=True))
Accessing Related Data	vessel.annual_analyses.all()
One-to-One (OneToOneField)	Filtering	Vessele.objects.filter(details__manufacturer="ABC Corp")
Q() Filtering	Vessele.objects.filter(Q(details__manufacturer="ABC Corp") & Q(details__build_year__gte=2000))
Accessing Related Data	vessel.details.manufacturer
Many-to-Many (ManyToManyField)	Filtering	Vessele.objects.filter(crew__name="John Doe")
Q() Filtering	`Vessele.objects.filter(Q(crew__name="John Doe")
Accessing Related Data	vessel.crew.all()

🚀 Key Takeaways
ForeignKey (One-to-Many)

Access via related_name (Vessele.annual_analyses).
Queries use modelname__fieldname.

OneToOneField (One-to-One)

Access via related_name (Vessele.deta
ils).
Ensures strict 1-to-1 relationship.
ManyToManyField (Many-to-Many)

Access via related_name (CrewMember.vesseles).
Queries work with multiple joins.


**Understanding crew__name in Django ORM Query**

result = Vessele.objects.filter(crew__name="John Doe")


Breaking Down crew__name
crew → Refers to the ManyToManyField relationship in the Vessele model that connects it to the CrewMember model.
name → A field in the CrewMember model that stores the name of the crew member.
crew__name="John Doe" → This means:
Join the Vessele table with the CrewMember table via the ManyToManyField relation.
Filter vessels where at least one associated crew member has the name "John Doe".

class CrewMember(models.Model):
    name = models.CharField(max_length=255)

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    crew = models.ManyToManyField(CrewMember, related_name="vesseles")



Here, each Vessele can have multiple CrewMember and each CrewMember can work on multiple Vessele.

Equivalent SQL Query
If Vessele and CrewMember have a many-to-many relationship through an intermediary table (vesselele_crew), Django ORM translates the query into:
    
SELECT v.*
FROM vessele v
JOIN vessele_crew vc ON v.vesseled_id = vc.vessele_id
JOIN crew_member c ON vc.crew_id = c.id
WHERE c.name = 'John Doe';

Joins Vessele with CrewMember via the many-to-many table.
Filters vessels where a crew member has name = "John Doe".

Alternative Queries

crew_member = CrewMember.objects.get(name="John Doe")
vessels = crew_member.vesseles.all()


Fetches all vessels where John Doe is a crew member.


q)Filtering Vessels Without a Specific Crew Member
Vessele.objects.exclude(crew__name="John Doe")
Returns all vessels where "John Doe" is NOT a crew member.

q)Finding Vessels with No Crew Members

Vessele.objects.filter(crew__isnull=True)

Returns all vessels that do not have any crew members.

 Key Takeaways
crew__name="John Doe" → Filters vessels that have at least one crew member named "John Doe".
Many-to-Many relationships use an intermediate table, and Django ORM automatically joins it when filtering.
You can reverse the relationship using related_name (e.g., CrewMember.vesseles.all()).


Middleware in Python (Django context)
In the context of Django, middleware refers to a layer of processing that sits between the request and response cycle.
 It is a mechanism that allows developers to hook into the request/response processing of Django.
 Middleware components are executed in the request-response cycle before the request reaches the view and after the view has processed the response.
 
 
 What Does Middleware Do?
Middleware is used for global request or response processing, such as modifying the request or response objects, handling sessions, logging, managing security, etc.
It allows the user to intercept and modify HTTP requests and responses in a flexible way.
How Middleware Works:
Request Phase:

When a request comes to Django, it passes through all the middleware in the order they are defined in MIDDLEWARE settings.
Each middleware has a chance to process the request before it reaches the view.
View Phase:

After passing through the middleware, the request reaches the view, which processes the request and returns a response.
Response Phase:

Once the view has generated a response, it passes through all the middleware in reverse order before being sent to the client.
Key Middleware Actions:
Before View Execution:

You can inspect, modify, or reject the request, for example, adding security checks or modifying headers.
After View Execution:

After the view returns a response, middleware can modify or inspect the response, for example, adding headers, logging, or modifying cookies.

How to Implement Middleware in Django


1. Defining a Simple Middleware Class
A basic middleware class in Django consists of two methods:

__init__(self, get_response) — Initializes the middleware.
__call__(self, request) — This method is executed for every request and response cycle.
Example of a custom middleware that adds a custom header:

# middleware.py

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to process the request before the view is called
        print("Request received")

        # Call the next middleware or the view
        response = self.get_response(request)

        # Code to process the response after the view is called
        response['X-Custom-Header'] = 'This is a custom header'

        return response


2. Registering Middleware in Settings
To enable the middleware in your Django project, add it to the MIDDLEWARE setting in settings.py.


# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yourapp.middleware.CustomMiddleware',  # Register your custom middleware here
]



3. Order of Middleware Execution
The order of middleware in MIDDLEWARE is important:

Middlewares at the top will execute first during the request phase and last during the response phase.
Middlewares at the bottom will execute last during the request phase and first during the response phase.


Common Use Cases for Middleware in Django
Request Processing:

Modify or inspect the request before it reaches the view.
Example: Checking user authentication or logging the request.
Response Processing:

Modify or inspect the response before it is sent to the client.
Example: Adding security headers or cookies.
Session Management:

Handle user sessions and cookies.
Error Handling:

Capture exceptions and modify error responses, such as handling 404 or 500 errors.
Cross-Origin Resource Sharing (CORS):

Adding appropriate headers for CORS to handle requests from different domains.
Custom Authentication or Authorization:

You can create middleware to enforce custom authentication or authorization logic before the request reaches the view.


Django Built-in Middleware
Django comes with several built-in middleware components, each serving a different purpose. Some common ones include:

SecurityMiddleware: Provides several security features like enforcing HTTPS (SECURE_SSL_REDIRECT) or handling content security policies.
SessionMiddleware: Manages user sessions, storing session data in the database or cookies.
CsrfViewMiddleware: Prevents Cross-Site Request Forgery (CSRF) attacks by checking for a valid CSRF token in forms and requests.
AuthenticationMiddleware: Associates the current request with the User object (if the user is authenticated).
CommonMiddleware: Implements various common tasks, like adding trailing slashes or preventing URL redirection loops.
MessageMiddleware: Handles storing messages in the session for the user (used for feedback messages).



Example of Middleware for Logging

# middleware.py

import logging

class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django')

    def __call__(self, request):
        # Log request details
        self.logger.info(f"Request: {request.method} {request.path}")
        
        # Proceed to the next middleware or view
        response = self.get_response(request)
        
        # Log response status
        self.logger.info(f"Response Status: {response.status_code}")
        
        return response



To log requests and responses, you'd add this middleware to the MIDDLEWARE setting in settings.py.



Key Takeaways:
Middleware is a powerful feature in Django for modifying requests and responses globally.
It is executed in a specific order, allowing developers to manage various cross-cutting concerns (e.g., security, logging, sessions).
You can create custom middleware by defining a class with __init__ and __call__ methods, processing requests before and after they reach the view.
Django provides many built-in middleware classes, and you can also write your own for specific needs.




The method __str__(self) is a special method in Python that defines how an instance of a class (in this case, a Django model) is
 represented as a string. This method is often used to provide a human-readable representation of the object, which is helpful for 
 debugging, displaying the object in the Django admin interface, or when you convert the object to a string (e.g., str(instance)).

In your case, the method:

def __str__(self):
    return self.user.username

Explanation:
self.user: Refers to an instance variable user that is most likely a ForeignKey relation to the User model or a related model in Django. 
This typically means the model has a user field that refers to a User object.
.username: Refers to the username field of the User model. In Django, the User model usually has a field called username that stores the username of a user.



Contextual Example:
If this code is in a model like the following:


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


Here:

The Profile model has a user field, which is a OneToOneField to the User model.
The __str__() method will return the username of the associated User when you convert an instance of the Profile model to a string.

Why Use __str__(self)?
Readability: When you print or display a Profile object, instead of showing an internal memory address (e.g., <Profile object at 0x12345>),
 it will display the username of the associated user.
 
 
 For example, if you run:
 
 profile = Profile.objects.get(id=1)
print(profile)


It will print something like:
    
johndoe



You need to join the two tables (vessele and annual_vessele_analysis) to fetch vesseled_id, ve_name, plaenty, and year. Here's the SQL query for that:

SELECT 
    v.vesseled_id AS vessile_id, 
    v.ve_name, 
    ava.plaenty, 
    ava.year
FROM vessele v
JOIN annual_vessele_analysis ava 
    ON v.vesseled_id = ava.vessile_id;



Explanation:
vesseled_id is used as the primary key in vessele and as a foreign key (vessile_id) in annual_vessele_analysis.
We perform an INNER JOIN on vesseled_id and vessile_id to get the required details.
The query selects and renames vesseled_id as vessile_id, retrieves ve_name from vessele, and fetches plaenty and year from annual_vessele_analysis.


If you're using Django ORM, you can write the query like this:

from django.db.models import Q
from your_app.models import Vessele, AnnualVesseleAnalysis

# Query to join Vessele with AnnualVesseleAnalysis where plaenty and year are NULL
result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
).values(
    'vesseled_id', 've_name', 'annualvesseleanalysis__plaenty', 'annualvesseleanalysis__year'
)

# Output the result
for row in result:
    print(row)



Explanation:
Vessele.objects.filter(...) → Filters Vessele records where plaenty and year in AnnualVesseleAnalysis are NULL.
values(...) → Selects only the required fields:
vesseled_id from Vessele
ve_name from Vessele
plaenty and year from AnnualVesseleAnalysis
Foreign Key Reference:
Assuming Vessele and AnnualVesseleAnalysis are related via a ForeignKey, Django automatically creates a reverse relation using lowercased model name (annualvesseleanalysis).




Here’s a complete Django project structure that includes:

Models for Vessele and AnnualVesseleAnalysis
Serializer to convert queryset data to JSON
Views with a GET API to fetch vessels where plaenty and year are NULL
URLs to expose the API




1️⃣ Project Structure
vessel_project/
│── vessel_app/
│   │── migrations/
│   │── __init__.py
│   │── models.py
│   │── serializers.py
│   │── views.py
│   │── urls.py
│── vessel_project/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── manage.py



2️⃣ Models (models.py)
from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    doc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ve_name

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_analyses")
    plaenty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.year}"


3️⃣ Serializer (serializers.py)

from rest_framework import serializers
from .models import Vessele, AnnualVesseleAnalysis

class AnnualVesseleAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualVesseleAnalysis
        fields = ['plaenty', 'year']

class VesseleSerializer(serializers.ModelSerializer):
    annual_analyses = AnnualVesseleAnalysisSerializer(many=True, read_only=True)

    class Meta:
        model = Vessele
        fields = ['vesseled_id', 've_name', 'annual_analyses']


4️⃣ Views (views.py)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vessele
from .serializers import VesseleSerializer

@api_view(['GET'])
def get_vessels_with_null_analysis(request):
    # Filter vessels where related AnnualVesseleAnalysis has plaenty and year as NULL
    vessels = Vessele.objects.filter(annual_analyses__plaenty__isnull=True, annual_analyses__year__isnull=True).distinct()
    
    # Serialize the queryset
    serializer = VesseleSerializer(vessels, many=True)
    
    return Response(serializer.data)


5️⃣ URLs (urls.py in vessel_app)
from django.urls import path
from .views import get_vessels_with_null_analysis

urlpatterns = [
    path('vessels-null/', get_vessels_with_null_analysis, name='vessels-null'),
]


6️⃣ Global URLs (urls.py in vessel_project)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vessel_app.urls')),
]


7️⃣ Install Required Packages

Make sure you have Django and Django REST Framework installed:

pip install django djangorestframework


8️⃣ Run the Server
python manage.py runserver


Now, the API is available at:
    
    
http://127.0.0.1:8000/api/vessels-null/



9️⃣ Example API Response
If there are vessels with plaenty and year as NULL, the JSON response will be:


[
    {
        "vesseled_id": 1,
        "ve_name": "Titanic",
        "annual_analyses": [
            {
                "plaenty": null,
                "year": null
            }
        ]
    }
]



🔹 Steps to Deploy Django on AWS



1️⃣ Set Up an EC2 Instance
Launch an EC2 instance

Go to AWS EC2 Dashboard → Launch Instance
Choose an Ubuntu 22.04 LTS or Amazon Linux 2 AMI.
Select t2.micro (free tier) or a higher instance type.
Configure security groups:
Allow SSH (22) from your IP
Allow HTTP (80) and HTTPS (443)
Attach an Elastic IP (optional, but recommended).
Connect to your EC2 instance
Open your terminal and connect via SSH:
    

ssh -i your-key.pem ubuntu@your-ec2-public-ip


2️⃣ Install Required Packages
Once connected to your EC2 instance, update packages and install dependencies:

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-dev libpq-dev nginx git -y


3️⃣ Set Up Virtual Environment & Install Django

sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework gunicorn psycopg2-binary


4️⃣ Clone Your Django Project

If your project is on GitHub, clone it:
    
git clone https://github.com/your-username/vessel_project.git
cd vessel_project
pip install -r requirements.txt


5️⃣ Configure PostgreSQL (AWS RDS)
Create an RDS instance

Go to AWS RDS Dashboard → Create Database
Choose PostgreSQL
Select Free-tier or desired instance type
Configure DB name, username, and password.
Allow your EC2's security group in the database security group.
Update settings.py in Django Replace the default database settings:
 
 
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your-db-instance.rds.amazonaws.com',
        'PORT': '5432',
    }
}


Run migrations
python manage.py migrate



6️⃣ Collect Static Files & Run Django
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000


Test if your Django app is running by opening:
 http://your-ec2-public-ip:8000
 
 
 
 7️⃣ Set Up Gunicorn
Install and test Gunicorn:
    
    
    pip install gunicorn
gunicorn --bind 0.0.0.0:8000 vessel_project.wsgi


If it's working, stop it (CTRL+C) and create a system service for it.

Create a Gunicorn service:
   sudo nano /etc/systemd/system/gunicorn.service

Add the following:
    [Unit]
Description=Gunicorn instance for Django project
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/vessel_project
ExecStart=/home/ubuntu/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/vessel_project.sock vessel_project.wsgi:application

[Install]
WantedBy=multi-user.target


Save & exit. Then restart the service:
    
    sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

8️⃣ Set Up Nginx

Create an Nginx config file

sudo nano /etc/nginx/sites-available/vessel_project


Add the following configuration

server {
    listen 80;
    server_name your-ec2-public-ip;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/vessel_project.sock;
    }
}



Enable the configuration
sudo ln -s /etc/nginx/sites-available/vessel_project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx


Now, you can access your Django project at:
    http://your-ec2-public-ip


9️⃣ Set Up a Domain Name & SSL (Optional)
Point a domain to EC2's Elastic IP using Route 53.

Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

Certbot will automatically configure Nginx for SSL.

🔹 Deployment Complete!
Your Django project is now fully deployed on AWS EC2 with Nginx, Gunicorn, and PostgreSQL. 🚀


🔹 Future Improvements
Use AWS S3 for static/media files
Set up a CI/CD pipeline with GitHub Actions
Use AWS Elastic Beanstalk for auto-scaling
Implement Docker & Kubernetes for containerization

    
    


🔹 @property Decorator in Python
The @property decorator in Python is used to define a getter method for a class attribute, making it behave like an attribute while still allowing customization of its behavior.

It allows:

Encapsulation – Provides controlled access to private variables.
Read-only Properties – Prevents direct modification of attributes.
Automatic Computation – Computes values dynamically.





q)

In Python, magic methods (also called dunder methods, short for "double underscore") are special methods that begin and end with double underscores (e.g., __init__, __str__). 
These methods enable operator overloading, custom behavior for built-in functions, and integration with Python’s object model.

Common Magic Methods:
Object Creation & Initialization
__new__(cls, *args, **kwargs): Controls instance creation before initialization.
__init__(self, ...): Initializes the object.

String Representation
__str__(self): Returns a string representation (used by print()).
__repr__(self): Returns an official string representation (used by repr()).

Arithmetic Operators
__add__(self, other): Implements self + other.
__sub__(self, other): Implements self - other.
__mul__(self, other): Implements self * other.
__truediv__(self, other): Implements self / other.
__floordiv__(self, other): Implements self // other.
__mod__(self, other): Implements self % other.
__pow__(self, other): Implements self ** other.


Comparison Operators
__eq__(self, other): Implements self == other.
__ne__(self, other): Implements self != other.
__lt__(self, other): Implements self < other.
__le__(self, other): Implements self <= other.
__gt__(self, other): Implements self > other.
__ge__(self, other): Implements self >= other.

Indexing, Slicing, and Iteration
__getitem__(self, key): Enables indexing (obj[key]).
__setitem__(self, key, value): Enables assignment (obj[key] = value).
__delitem__(self, key): Enables deletion (del obj[key]).
__iter__(self): Enables iteration (for x in obj:).
__next__(self): Defines iteration behavior.

Attribute Access
__getattr__(self, name): Called when accessing a missing attribute.
__setattr__(self, name, value): Controls setting an attribute.
__delattr__(self, name): Controls deletion of an attribute.
Object Context (with with statement)
__enter__(self): Defines behavior when entering a context.
__exit__(self, exc_type, exc_value, traceback): Defines behavior when exiting.





    
