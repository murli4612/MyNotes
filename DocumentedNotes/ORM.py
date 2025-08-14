The following models represent vessels and their annual analysis.

🔹 Vessele Model (Represents Ships/Vessels)

from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)  # Name of the vessel

    def __str__(self):
        return self.ve_name


vesseled_id: Unique identifier for each vessel (Primary Key).
ve_name: Name of the vessel.
🔹 AnnualVesseleAnalysis Model (Stores Analysis of Each Vessel)

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annualvesseleanalysis")
    plaenty = models.CharField(max_length=255, null=True, blank=True)  # Can be NULL
    year = models.IntegerField(null=True, blank=True)  # Can be NULL

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.year}"
        
        
vessele (ForeignKey to Vessele): Links this analysis to a specific vessel.
plaenty (String, nullable): Stores penalties (or some analysis info).
year (Integer, nullable): The year of the analysis.

2️⃣ Query Breakdown

from django.db.models import Q
from your_app.models import Vessele, AnnualVesseleAnalysis

# Query: Find all vessels where the associated AnnualVesseleAnalysis has NULL 'plaenty' and NULL 'year'
result = Vessele.objects.filter(
    annualvesseleanalysis__plaenty__isnull=True,
    annualvesseleanalysis__year__isnull=True
).values(
    'vesseled_id', 've_name', 'annualvesseleanalysis__plaenty', 'annualvesseleanalysis__year'
)

🔹 What This Query Does
Joins Vessele with AnnualVesseleAnalysis using ForeignKey.
Filters vessels where both plaenty and year are NULL.
Returns results in dictionary format (.values()).

3️⃣ Sample Data Representation
🔹 Vessele Table (Ships)

vesseled_id	ve_name
1	        Ship A
2	        Ship B
3	        Ship C

🔹 AnnualVesseleAnalysis Table (Analysis Data)

id	vessele_id	plaenty	year
1	1	         NULL	NULL
2	1	         Fine	2023
3	2	         NULL	NULL
4	3	         Warning	2022



🔹 Expected Query Output
vesseled_id	ve_name	  annualvesseleanalysis__plaenty	annualvesseleanalysis__year
1	        Ship A	  NULL	                                NULL
2	        Ship B	  NULL                                  NULL


Ship A appears because at least one of its analyses has plaenty=NULL and year=NULL.
Ship C is not included since it has a non-null analysis record.
Ship B is included since all its records meet the condition.


4️⃣ Optimizing the Query
If you want only vessels where ALL records have NULL values, use aggregation:


from django.db.models import Count

Vessele.objects.annotate(
    null_entries=Count('annualvesseleanalysis', filter=Q(annualvesseleanalysis__plaenty__isnull=True, annualvesseleanalysis__year__isnull=True))
).filter(
    null_entries__gt=0
).values('vesseled_id', 've_name')




What is Meant by Optimizing a Query?
Optimizing a query means improving its performance by reducing execution time, memory usage, or database load while still returning the correct results.


🔹 Why Optimize Queries?
Faster execution: Reduces response time, which is critical in large databases.
Less CPU and memory usage: Queries that take longer consume more database resources.
Better scalability: Optimized queries handle more users and requests efficiently.
Reduced database locks: Helps avoid slowing down other queries.

🔹 How to Optimize Django Queries?
1️⃣ Use .values() Instead of Fetching Full Objects
👉 Fetching only required fields avoids unnecessary data retrieval.

# BAD: Fetches entire model objects (unnecessary fields)
vessels = Vessele.objects.all()

# GOOD: Fetches only required fields
vessels = Vessele.objects.values('vesseled_id', 've_name')


✅ This avoids the overhead of fetching full objects when only specific fields are needed.

2️⃣ Use .select_related() for ForeignKey Joins
👉 Avoids multiple queries by using a SQL JOIN instead of separate queries.


# BAD: Causes an extra query for each related object
vessels = Vessele.objects.all()
for vessel in vessels:
    print(vessel.annualvesseleanalysis_set.all())  # Triggers extra queries

# GOOD: Uses JOIN to fetch related data in a single query
vessels = Vessele.objects.select_related('annualvesseleanalysis').all()


✅ This reduces the number of database hits.


3️⃣ Use .prefetch_related() for Many-to-Many & Reverse Relations
👉 Efficiently fetches related objects in two queries instead of multiple.

# BAD: Causes N queries (1 per related object)
vessels = Vessele.objects.all()
for vessel in vessels:
    print(vessel.annualvesseleanalysis_set.all())

# GOOD: Uses prefetching (fetches all at once)
vessels = Vessele.objects.prefetch_related('annualvesseleanalysis').all()



✅ This is helpful when dealing with One-to-Many or Many-to-Many relations.

4️⃣ Avoid COUNT(*) Queries for Checking Existence
👉 Use .exists() instead of .count() to check if records exist.

# BAD: Unnecessary count operation (fetches all rows)
if Vessele.objects.filter(ve_name='Ship A').count() > 0:
    print("Exists")

# GOOD: Efficient query (stops at first match)
if Vessele.objects.filter(ve_name='Ship A').exists():
    print("Exists")

5️⃣ Use Database Indexing
👉 Indexing speeds up searches on frequently queried columns.


✅ Improves query speed for filtering and lookups.

6️⃣ Avoid Fetching Large Datasets
👉 Use pagination to load only needed data.

from django.core.paginator import Paginator

vessels = Vessele.objects.all()
paginator = Paginator(vessels, 10)  # 10 vessels per page

page_1_vessels = paginator.page(1)  # Fetch first 10 vessels

✅ This prevents loading large amounts of data into memory.

🔹 Key Takeaways
❌ Bad Practice                 	        ✅ Optimized Practice
Fetching all data with .all()	                 Use .values() for specific fields
Making separate queries for relations	         Use .select_related() or .prefetch_related()
Using .count() to check existence	              Use .exists()
Querying large data at once	                   Use pagination
No indexing                                  	Add db_index=True for frequently queried fields




Understanding the Given Django Query
This query is designed to find vessels (Vessele) that have at least one associated
 AnnualVesseleAnalysis record where both plaenty and year are NULL. Let's break it down step by step.
 
 1️⃣ Query Breakdown
 
 from django.db.models import Count, Q

Vessele.objects.annotate(
    null_entries=Count(
        'annualvesseleanalysis',  
        filter=Q(annualvesseleanalysis__plaenty__isnull=True, annualvesseleanalysis__year__isnull=True)
    )
).filter(
    null_entries__gt=0
).values('vesseled_id', 've_name')


2️⃣ Explanation of Each Part
✅ annotate(null_entries=Count(...))
This counts the number of related AnnualVesseleAnalysis records where both plaenty and year are NULL.
The filter=Q(...) inside Count ensures that we count only those records where both conditions (plaenty IS NULL and year IS NULL) are met.
✅ .filter(null_entries__gt=0)
Keeps only those Vessele entries where at least one AnnualVesseleAnalysis record matches the condition (i.e., null_entries > 0).
✅ .values('vesseled_id', 've_name')
Returns only the vesseled_id and ve_name fields (avoiding unnecessary data retrieval).


3️⃣ Example Data Representation
📌 Vessele Table
vesseled_id 	ve_name
1	            Ship A
2	            Ship B
3	              Ship C
📌 AnnualVesseleAnalysis Table
id	vessele_id  	plaenty 	year
1	1	NULL	NULL
2	1	Fine	2023
3	2	NULL	NULL
4	2	NULL	NULL
5	3	Tax	2022
📌 Query Output
vesseled_id	 ve_name
1	          Ship A
2	         Ship B


4️⃣ Optimized Version for Performance
If the dataset is large, consider adding an index on ForeignKey and NULL-check columns for faster lookups.
class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annualvesseleanalysis")
    plaenty = models.CharField(max_length=255, null=True, blank=True, db_index=True)  # ✅ Add Index
    year = models.IntegerField(null=True, blank=True, db_index=True)  # ✅ Add Index


Adding db_index=True on plaenty and year improves query speed significantly.


5️⃣ Summary
✅ The query retrieves only vessels with at least one NULL analysis entry.
✅ Uses Count() with Q() filter to efficiently count NULL values.
✅ Filters efficiently with .filter(null_entries__gt=0).
✅ Indexes on nullable columns improve performance.


Yes! You can retrieve columns from both the Vessele and AnnualVesseleAnalysis tables in the .values() method.

Here’s how you can modify your query to include fields from both tables:

Updated Query

from django.db.models import Count, Q

Vessele.objects.annotate(
    null_entries=Count(
        'annualvesseleanalysis',
        filter=Q(annualvesseleanalysis__plaenty__isnull=True, annualvesseleanalysis__year__isnull=True)
    )
).filter(
    null_entries__gt=0
).values(
    'vesseled_id',  # From Vessele Table
    've_name',      # From Vessele Table
    'annualvesseleanalysis__plaenty',  # From AnnualVesseleAnalysis
    'annualvesseleanalysis__year'      # From AnnualVesseleAnalysis
)


How It Works
Vessele.objects.annotate(...):
Counts AnnualVesseleAnalysis records where plaenty and year are NULL.
.filter(null_entries__gt=0):
Filters out vessels that don’t have any NULL records.
.values(...):
Retrieves fields from both tables using the related field lookup (annualvesseleanalysis__).


Example Output
vesseled_id	ve_name	plaenty	year
1	Ship A	NULL	NULL
2	Ship B	NULL	NULL



Understanding Q and distinct() in Django ORM

1. Q Objects in Django ORM
Q objects are used for complex queries involving OR conditions or dynamic filtering.

Example: Without Q
from django.db.models import Q
from your_app.models import Vessele

# Find vessels where 've_name' is 'Ship A' AND 'vesseled_id' is 1
Vessele.objects.filter(ve_name="Ship A", vesseled_id=1)

This performs an AND operation (ve_name="Ship A" AND vesseled_id=1).


Example: Using Q for OR conditions

Vessele.objects.filter(Q(ve_name="Ship A") | Q(vesseled_id=1))


This performs an OR operation (ve_name="Ship A" OR vesseled_id=1).

Using Q with Negation (~)
Vessele.objects.filter(~Q(ve_name="Ship A"))  # NOT condition

This filters all vessels except those named "Ship A"


Using Q for Complex Queries
Vessele.objects.filter(
    Q(ve_name="Ship A") & (Q(vesseled_id=1) | Q(vesseled_id=2))
)

Equivalent to:

SELECT * FROM Vessele
WHERE ve_name = 'Ship A' AND (vesseled_id = 1 OR vesseled_id = 2);


2. distinct() in Django ORM
The .distinct() method removes duplicate rows from query results.

Example: Without .distinct()


Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values('vesseled_id', 've_name')

If a vessel has multiple matching AnnualVesseleAnalysis rows, it will appear multiple times.


Using .distinct()

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values('vesseled_id', 've_name').distinct()

Now, each vesseled_id appears only once, even if multiple matching records exist.


When to Use .distinct()
To remove duplicate rows when using .values() or .values_list()
If joins create unintended duplicates
When selecting only certain columns (.values()) but need unique records
⚠️ Warning:

.distinct() applies to the entire row, so it may not work as expected if only selecting some fields.
Some databases (like PostgreSQL) allow .distinct('column_name'), but others (like MySQL) do not.

Combining Q and distinct()

Vessele.objects.filter(
    Q(ve_name="Ship A") | Q(vesseled_id=1),
    annualvesseleanalysis__plaenty__isnull=True
).values('vesseled_id', 've_name').distinct()



Filters vessels where ve_name="Ship A" OR vesseled_id=1
Ensures each vessel appears only once.

Final Takeaways
Feature	Purpose
Q	Used for complex filtering with OR, AND, NOT conditions
distinct()	Removes duplicate rows from query results


Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values('vesseled_id', 've_name')


is performing a JOIN between Vessele and AnnualVesselAnalysis tables using the foreign key relationship
 (assuming annualvesseleanalysis is a related name from AnnualVesselAnalysis to Vessele).
 
 Issue:
If there are multiple matching rows in AnnualVesselAnalysis for a single Vessele, it will return duplicate vesseled_id and ve_name values.
You want to include all columns from both tables without using distinct.

Solution 1: Fetch All Columns from Both Tables
To retrieve all columns from both tables, you should use values() with F() expressions to explicitly get columns from both tables.

from django.db.models import F

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values(
    'vesseled_id', 've_name',  
    'annualvesseleanalysis__id', 'annualvesseleanalysis__plaenty', 
    'annualvesseleanalysis__other_column1', 'annualvesseleanalysis__other_column2'
)

This will return all rows from both tables without using distinct().

Solution 2: Use select_related() or prefetch_related() for Better Performance
If you want to avoid multiple queries and efficiently fetch related data:
    
Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).select_related('annualvesseleanalysis')



OR
Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).prefetch_related('annualvesseleanalysis')



select_related() is used when annualvesseleanalysis is a ForeignKey.
prefetch_related() is used when annualvesseleanalysis is a reverse ForeignKey (One-to-Many relationship).

Based on your query, here’s how the database tables (Vessele and AnnualVesselAnalysis) are structured.

1. Vessele Table
vesseled_id (PK)	ve_name	      other_columns...
1	               Ship A	           ...
2	               Ship B	             ...
3	                Ship C	         ...


2. AnnualVesselAnalysis Table (Foreign Key to Vessele)
id (PK)   	vessele_id (FK)	    plaenty	    other_columns...
1	                  1         	NULL	  ...
2	1	Fine 1	...
3	2	NULL	...
4	3	Fine 2	...
Query Explanation

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values('vesseled_id', 've_name')


This means:

Fetch all vessels (Vessele) where at least one related AnnualVesselAnalysis entry has plaenty IS NULL.
Duplicates may occur if a vessel has multiple AnnualVesselAnalysis records matching the condition.
Query Output (Without distinct()):
 
vesseled_id	ve_name
1	Ship A
2	Ship B
Since Ship A and Ship B have at least one row in AnnualVesselAnalysis where plaenty IS NULL, they appear in the result.

Fetching All Columns Without distinct()
If you want all columns from both tables:
    

Query Output

vesseled_id	ve_name	id (Analysis)	plaenty
1	Ship A	1	NULL
2	Ship B	3	NULL


Some more records:
    
1. Vessele Table


vesseled_id (PK)	ve_name
1	                Ship A
2	                Ship B
3	                Ship C



2. AnnualVesselAnalysis Table (Foreign Key to Vessele)
This table now has multiple entries for the same vessel, some with plaenty = NULL.


id (PK)	vessele_id (FK)	plaenty
1	1	NULL
2	1	Fine 1
3	1	NULL
4	2	NULL
5	2	NULL
6	3	Fine 2
7	3	NULL
8	3	Fine 3


Query Without distinct()

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values('vesseled_id', 've_name')


Since Ship A and Ship B each have multiple plaenty = NULL entries, they appear multiple times in the result:
 
 vesseled_id	ve_name
1	Ship A
1	Ship A
2	Ship B
2	Ship B
3	Ship C

Query With distinct()

Now, the duplicates are removed:

vesseled_id	ve_name
1	Ship A
2	Ship B
3	Ship C


Fetching All Columns Without distinct()

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).values(
    'vesseled_id', 've_name', 'annualvesseleanalysis__id', 'annualvesseleanalysis__plaenty'
)


vesseled_id	ve_name	id (Analysis)	plaenty
1	Ship A	1	NULL
1	Ship A	3	NULL
2	Ship B	4	NULL
2	Ship B	5	NULL
3	Ship C	7	NULL


Fetching All Columns With distinct()



When using .distinct() in Django ORM, it applies to the entire selected row. However, since you are including fields
 from the related AnnualVesselAnalysis table, each row might still be unique due to different id values. 
That means .distinct() won't eliminate duplicates as expected.



Corrected Approach for Distinct Results
To correctly fetch distinct vessels along with related AnnualVesselAnalysis records, follow these methods:

1. Using .distinct() Properly (But Might Not Work as Expected)


Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True)
       .values('vesseled_id', 've_name', 'annualvesseleanalysis__id', 'annualvesseleanalysis__plaenty')
       .distinct()


🔴 Problem: This does not work as expected because each row still has a unique annualvesseleanalysis__id, making .distinct() ineffective


2. Group by vesseled_id (Selecting One Analysis Record per Vessel)
Use annotate(Min('annualvesseleanalysis__id')) to select only one related AnnualVesselAnalysis entry per vessel.


from django.db.models import Min

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True)
       .annotate(min_analysis_id=Min('annualvesseleanalysis__id'))
       .values('vesseled_id', 've_name', 'min_analysis_id')


✅ This ensures each vessel appears only once, but we only get one analysis ID (min_analysis_id).



3. Using Subquery to Fetch the First Matching Analysis Record
If you need all columns from AnnualVesselAnalysis but only one entry per vessel, use Subquery:
    

from django.db.models import Subquery, OuterRef

subquery = AnnualVesselAnalysis.objects.filter(
    vessele_id=OuterRef('vesseled_id'), plaenty__isnull=True
).order_by('id').values('id')[:1]  # Fetch the first matching analysis record

Vessele.objects.filter(annualvesseleanalysis__plaenty__isnull=True).annotate(
    analysis_id=Subquery(subquery)
).values('vesseled_id', 've_name', 'analysis_id')


✅ This returns only one AnnualVesselAnalysis record per vessel, avoiding duplicates.

Final Output (Corrected Version)
vesseled_id	ve_name	analysis_id
1	Ship A	1
2	Ship B	4
3	Ship C	7


q)The Django ORM query you provided translates to an SQL query that performs a JOIN between the 
Vessele and AnnualVesseleAnalysis tables, filtering records where plaenty and year are both NULL.


Equivalent SQL Query

SELECT 
    v.vesseled_id, 
    v.ve_name, 
    a.plaenty, 
    a.year
FROM Vessele v
JOIN AnnualVesseleAnalysis a 
    ON v.vesseled_id = a.vessele_id
WHERE 
    a.plaenty IS NULL 
    AND a.year IS NULL;



Breaking It Down
SELECT Clause:

Fetches vesseled_id, ve_name from the Vessele table.
Fetches plaenty and year from the AnnualVesseleAnalysis table.
JOIN Clause:

Inner Join (JOIN) ensures that only vessels with a matching AnnualVesseleAnalysis entry are considered.
The ON condition links the two tables using vessele_id (foreign key).
WHERE Clause:

Filters rows where both plaenty and year are NULL.



Understanding One-to-One Relationship (OneToOneField) in Django
In Django, a OneToOneField creates a one-to-one relationship between two models, meaning that each record in 
one table corresponds to exactly one record in another table.


📌 Given Models:
    
from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ve_name

class VesseleDetails(models.Model):
    vessele = models.OneToOneField(Vessele, on_delete=models.CASCADE, related_name="details")
    manufacturer = models.CharField(max_length=255)
    build_year = models.IntegerField()

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.manufacturer}"


Vessele Table: Stores vessel information.
VesseleDetails Table: Stores detailed information about a vessel (one-to-one relationship).
Foreign Key (OneToOneField): vessele in VesseleDetails references Vessele via related_name="details".
This allows access to details via vesseled_obj.details in Django ORM.



📌 Data Representation in Tables
Vessele Table

vesseled_id	ve_name
1	Titan
2	Atlantic
3	Pacific

VesseleDetails Table
id	vessele_id	manufacturer	build_year
1	1	ABC Corp	2000
2	2	XYZ Ltd	2010
3	3	ABC Corp	2015


📌 Query: Filtering Vessels by Manufacturer

result = Vessele.objects.filter(details__manufacturer="ABC Corp")


🔹 Equivalent SQL Query

SELECT v.vesseled_id, v.ve_name
FROM Vessele v
JOIN VesseleDetails d ON v.vesseled_id = d.vessele_id
WHERE d.manufacturer = 'ABC Corp';



🔹 Query Execution Breakdown
Vessele.objects.filter(details__manufacturer="ABC Corp")

Uses related_name (details) to filter vessels based on their details.
Looks for vessels where manufacturer = "ABC Corp".
JOINs Vessele with VesseleDetails:

Since VesseleDetails has a OneToOneField, each Vessele has at most one corresponding detail.
Filtered Output (Matching Manufacturer = "ABC Corp"):

Titan (ID 1) → ABC Corp
Pacific (ID 3) → ABC Corp


📌 Expected Query Output
vesseled_id	ve_name
1	Titan
3	Pacific


🔹 Alternative Query: Get VesseleDetails Instead
If you want to fetch details instead of vessels:
    
result = VesseleDetails.objects.filter(manufacturer="ABC Corp").values('vessele__vesseled_id', 'vessele__ve_name', 'manufacturer', 'build_year')



SQL Equivalent:
    
 SELECT v.vesseled_id, v.ve_name, d.manufacturer, d.build_year
FROM VesseleDetails d
JOIN Vessele v ON d.vessele_id = v.vesseled_id
WHERE d.manufacturer = 'ABC Corp';

Output:
    

vesseled_id	ve_name	manufacturer	build_year
1	Titan	ABC Corp	2000
3	Pacific	ABC Corp	2015


🚀 Key Takeaways
OneToOneField creates a strict 1:1 mapping between two tables.
You can filter data using related_name (details__manufacturer) to join and query efficiently.
Django ORM automatically performs JOINs in the background.
SQL equivalent query uses INNER JOIN to fetch matching records.


Understanding OneToOneField Access in Django ORM
In Django, when you define a OneToOneField, you create a one-to-one relationship between two models. 
This means that each row in one table corresponds to exactly one row in another table.


📌 Given Models
from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ve_name

class VesseleDetails(models.Model):
    vessele = models.OneToOneField(Vessele, on_delete=models.CASCADE, related_name="details")
    manufacturer = models.CharField(max_length=255)
    build_year = models.IntegerField()

    def __str__(self):
        return f"{self.vessele.ve_name} - {self.manufacturer}"


📌 Query Explanation

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)  # Accessing OneToOneField


vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)  # Accessing OneToOneField


🔹 Step-by-Step Execution
1)Retrieve the Vessele record

vessel = Vessele.objects.get(vesseled_id=1)

This fetches a Vessele object where vesseled_id = 1.

2)Access related VesseleDetails

vessel.details


Since we defined OneToOneField with related_name="details", we can access the corresponding VesseleDetails record directly via vessel.details.

3)Retrieve the manufacturer field from VesseleDetails

vessel.details.manufacturer

This fetches the manufacturer name from the related VesseleDetails table.

📌 Example Data in Tables
Vessele Table

vesseled_id	ve_name
1	Titan
2	Atlantic
3	Pacific


VesseleDetails Table
id	vessele_id	manufacturer	build_year
1	1	ABC Corp	2000
2	2	XYZ Ltd	2010
3	3	ABC Corp	2015



📌 Example Execution

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)


🔹 Output

ABC Corp


Explanation:

vesseled_id = 1 corresponds to "Titan".
"Titan" has one related record in VesseleDetails with manufacturer = "ABC Corp".
Using vessel.details.manufacturer, we fetch "ABC Corp".


📌 SQL Equivalent Query
If we break down the query execution in SQL, Django ORM internally performs:
SELECT d.manufacturer 
FROM VesseleDetails d
JOIN Vessele v ON d.vessele_id = v.vesseled_id
WHERE v.vesseled_id = 1;


📌 Key Takeaways
✅ OneToOneField ensures a 1:1 relationship between Vessele and VesseleDetails.
✅ Using related_name="details", we can access VesseleDetails directly via Vessele.
✅ Django ORM automatically performs JOINs, making data retrieval seamless.


q)if we write this vessel = Vessele.objects.get(vesseled_id=1), then it will result from both table


No, the query vessel = Vessele.objects.get(vesseled_id=1) only fetches data from the Vessele table, not from the VesseleDetails table.

However, Django provides automatic relation access through the OneToOneField (related_name="details"), allowing you to retrieve related data lazily (on demand).

📌 Breaking Down the Query Execution
vessel = Vessele.objects.get(vesseled_id=1)


✅ What happens here?

This retrieves only the Vessele object with vesseled_id = 1 from the Vessele table.
🚫 What does NOT happen?

No data is fetched from the VesseleDetails table yet.
The manufacturer or build_year fields are not retrieved at this stage.


📌 Fetching Data from VesseleDetails
If you try to access vessel.details, Django will then query the VesseleDetails table using a separate SQL query.

print(vessel.details.manufacturer)  # Now, Django queries VesseleDetails



✅ Now, Django executes a second query to fetch VesseleDetails where vessele_id = 1.
✅ Since we used related_name="details", we can access VesseleDetails via vessel.details.


📌 Equivalent SQL Queries
1️⃣ First Query (Fetching only from Vessele)

SELECT * FROM Vessele WHERE vesseled_id = 1;


2️⃣ Second Query (Fetching Related VesseleDetails on Access)

SELECT * FROM VesseleDetails WHERE vessele_id = 1;


🔹 Django executes two queries instead of a single JOIN query because it follows a lazy-loading approach for related objects.


📌 Fetching Data from Both Tables in a Single Query
If you want to fetch data from both Vessele and VesseleDetails in one query, use select_related:

vessel = Vessele.objects.select_related("details").get(vesseled_id=1)
print(vessel.details.manufacturer)  # No extra query here!



✅ Django now fetches data from both tables in a single query:
    
SELECT v.*, d.manufacturer, d.build_year
FROM Vessele v
LEFT JOIN VesseleDetails d ON v.vesseled_id = d.vessele_id
WHERE v.vesseled_id = 1;

📌 Summary
Query	                                                             Data Retrieved	       SQL Query Type
Vessele.objects.get(vesseled_id=1)	                             Only Vessele	         Single-table SELECT
vessel.details.manufacturer	                                Triggers second query for VesseleDetails	Separate SELECT
Vessele.objects.select_related("details").get(vesseled_id=1)	Data from both tables in one query            	Uses JOIN
✅ Use select_related("details") to optimize performance when accessing related data.


📌 How select_related Optimizes Performance in Django ORM
select_related optimizes database performance by reducing the number of queries when fetching related objects.

1️⃣ Problem with Lazy Loading (Without select_related)
By default, Django ORM lazy-loads related data.
This means it executes separate SQL queries each time you access related fields.

Example Without select_related:


vessels = Vessele.objects.all()  # Fetches all vessels

for vessel in vessels:
    print(vessel.details.manufacturer)  # Triggers extra queries!


🔴 Query Execution (Inefficient)


SELECT * FROM Vessele;  -- 1st Query: Fetches all vessels
SELECT * FROM VesseleDetails WHERE vessele_id = 1; -- 2nd Query
SELECT * FROM VesseleDetails WHERE vessele_id = 2; -- 3rd Query
...

❌ This results in the "N+1 Query Problem" → 1 main query + N additional queries
❌ If there are 100 vessels, Django will execute 101 queries!


2️⃣ Solution: Using select_related (Eager Loading)
Instead of executing multiple queries, select_related uses SQL JOIN to fetch all data in one optimized query.

Example With select_related:
    
vessels = Vessele.objects.select_related("details").all()  # Fetches vessels + details in one query

for vessel in vessels:
    print(vessel.details.manufacturer)  # No extra queries!


vessels = Vessele.objects.select_related("details").all()  # Fetches vessels + details in one query

for vessel in vessels:
    print(vessel.details.manufacturer)  # No extra queries!


✅ Optimized Query Execution

SELECT v.*, d.manufacturer, d.build_year 
FROM Vessele v
LEFT JOIN VesseleDetails d ON v.vesseled_id = d.vessele_id;


✅ Only 1 query instead of N queries!
✅ Faster performance, especially when fetching large datasets!

3️⃣ Performance Comparison: Without vs. With select_related

Scenario	Number of Queries	Query Type	Performance
Vessele.objects.all()	1 + N Queries	Multiple SELECT	Slow ❌
Vessele.objects.select_related("details").all()	1 Query	JOIN Query	Fast 🚀


4️⃣ When to Use select_related?
🔹 Use select_related for One-to-One (OneToOneField) or Foreign Key (ForeignKey) relationships.
🔹 Best when you always need related data (e.g., fetching details for all vessels).
🔹 Avoid using it for many-to-many relationships (ManyToManyField), as it can lead to huge joins.


✅ Summary
Without select_related → Django runs multiple queries (N+1 Query Problem).
With select_related → Django runs one SQL JOIN query, reducing database hits.
Best for ForeignKey & OneToOneField to improve performance in large datasets.


📌 Difference Between OneToOneField and ForeignKey in Django ORM
Both OneToOneField and ForeignKey define relationships between models in Django, 
but they behave differently in terms of cardinality (one-to-one vs. one-to-many). Let's break it down. 👇


1️⃣ OneToOneField (One-to-One Relationship)
Definition: Each record in Model A must have exactly one matching record in Model B.
Behavior: Similar to a ForeignKey with unique=True.
Use Case: When one record should be directly linked to another.


Example: Vessele and VesseleDetails (One-to-One)
Each vessel has one set of details.

from django.db import models

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

class VesseleDetails(models.Model):
    vessele = models.OneToOneField(Vessele, on_delete=models.CASCADE, related_name="details")
    manufacturer = models.CharField(max_length=255)
    build_year = models.IntegerField()


Behavior:
Each vessel has exactly one VesseleDetails.
You can access details directly:


vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.details.manufacturer)  # ✅ Direct access


This prevents multiple details for the same vessel.


SQL Equivalent (OneToOneField)

CREATE TABLE Vessele (
    vesseled_id SERIAL PRIMARY KEY,
    ve_name VARCHAR(255)
);

CREATE TABLE VesseleDetails (
    id SERIAL PRIMARY KEY,
    vessele_id INT UNIQUE REFERENCES Vessele(vesseled_id) ON DELETE CASCADE,
    manufacturer VARCHAR(255),
    build_year INT
);


☑ UNIQUE constraint ensures one-to-one relationship.


2️⃣ ForeignKey (One-to-Many Relationship)
Definition: Each record in Model B can be linked to multiple records in Model A.
Behavior: A single parent object can have many child objects.
Use Case: When one record should be associated with multiple records.
Example: Vessele and AnnualVesseleAnalysis (One-to-Many)
Each vessel can have multiple annual analyses.


class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)


Behavior:
A vessel can have many reports:

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.annual_reports.all())  # ✅ Returns a QuerySet (multiple entries)

Unlike OneToOneField, multiple records are allowed.

SQL Equivalent (ForeignKey)

CREATE TABLE AnnualVesseleAnalysis (
    id SERIAL PRIMARY KEY,
    vessele_id INT REFERENCES Vessele(vesseled_id) ON DELETE CASCADE,
    plaenty VARCHAR(255),
    year INT
);



☑ No UNIQUE constraint, so multiple analyses per vessel are allowed.

3️⃣ Key Differences Between OneToOneField and ForeignKey
Feature	OneToOneField	ForeignKey
Cardinality	One-to-One	One-to-Many
Example Use Case	Vessel → VesselDetails	Vessel → Annual Analysis
Database Constraint	UNIQUE constraint	No UNIQUE, allows multiple rows
Accessing Data	vessel.details (Single object)	vessel.annual_reports.all() (QuerySet)
Reverse Lookup	related_name="details"	related_name="annual_reports"


4️⃣ When to Use Which?
✅ Use OneToOneField when each object in Table A must have exactly one related object in Table B
✅ Use ForeignKey when one object in Table A can be related to multiple objects in Table B



5️⃣ Real-World Analogy
🔹 OneToOneField → Person & Passport (Each person has only one passport).
🔹 ForeignKey → Customer & Orders (One customer can place multiple orders).

✅ Summary
OneToOneField is like a ForeignKey with unique=True (1-to-1).
ForeignKey allows 1-to-many relationships.
Both use on_delete=models.CASCADE to handle deletions.
Use select_related() with OneToOneField to optimize performance.


3️⃣ Many-to-Many Relationship (ManyToManyField)
A record in Table A can be related to multiple records in Table B, and vice versa.

Example:
A Vessel can have multiple owners, and an Owner can own multiple vessels.


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    owners = models.ManyToManyField(Owner, related_name="vessels")


SQL Equivalent
Django automatically creates a junction table to handle the Many-to-Many relationship.

CREATE TABLE Vessele_Owners (
    id SERIAL PRIMARY KEY,
    vessele_id INT REFERENCES Vessele(vesseled_id) ON DELETE CASCADE,
    owner_id INT REFERENCES Owner(owner_id) ON DELETE CASCADE
);



Accessing Data

owner = Owner.objects.get(owner_id=1)
print(owner.vessels.all())  # ✅ Returns all vessels owned by the owner

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.owners.all())  # ✅ Returns all owners of the vessel


Adding and Removing Data

vessel.owners.add(owner)  # ✅ Assign an owner to the vessel
vessel.owners.remove(owner)  # ✅ Remove an owner


4️⃣ Reverse Foreign Key (related_name)
If a model has a ForeignKey, we can access related objects using related_name.

Example:
A Vessel has multiple Annual Analyses, and we want to fetch them.

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)


Accessing Reverse Foreign Key

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.annual_reports.all())  # ✅ Returns all related AnnualVesseleAnalysis


Without related_name, we would have used annualvesseleanalysis_set.all().
related_name makes querying cleaner.

5️⃣ Performance Optimization (select_related() & prefetch_related())
🔹 select_related(): Optimizes One-to-One & ForeignKey relationships by using SQL JOIN.
🔹 prefetch_related(): Optimizes Many-to-Many & Reverse Foreign Key relationships.

Example:


vessels = Vessele.objects.select_related("details").all()  # ✅ Uses JOIN (Fast for One-to-One & ForeignKey)
owners = Vessele.objects.prefetch_related("owners").all()  # ✅ Uses separate queries (Fast for Many-to-Many)


📌 Summary Table

Relationship	Field Type	SQL Behavior	Query Example
One-to-One	OneToOneField	Adds UNIQUE constraint	vessel.details.manufacturer
One-to-Many	ForeignKey	Multiple records in child table	vessel.annual_reports.all()
Many-to-Many	ManyToManyField	Creates a junction table	vessel.owners.all()
Reverse Foreign Key	related_name="X"	Enables reverse lookup	vessel.annual_reports.all()


🚀 Final Thoughts
✅ Use OneToOneField when there must be exactly one related record.
✅ Use ForeignKey when one object can have multiple related objects.
✅ Use ManyToManyField when both sides can have multiple relationships.
✅ Use select_related() & prefetch_related() for performance optimization.



1️⃣ Many-to-Many Relationship (ManyToManyField)
A record in Table A can be related to multiple records in Table B, and vice versa.

Example: Vessel & Owner
A Vessel can have multiple Owners.
An Owner can own multiple Vessels.
Django Models

from django.db import models

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    owners = models.ManyToManyField(Owner, related_name="vessels")



SQL Equivalent
Django automatically creates a junction table (Vessele_owners) to manage the many-to-many relationship.


CREATE TABLE Owner (
    owner_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Vessele (
    vesseled_id SERIAL PRIMARY KEY,
    ve_name VARCHAR(255)
);

CREATE TABLE Vessele_owners (  -- Junction Table
    id SERIAL PRIMARY KEY,
    vessele_id INT REFERENCES Vessele(vesseled_id) ON DELETE CASCADE,
    owner_id INT REFERENCES Owner(owner_id) ON DELETE CASCADE
);


Data Representation
Owner Table

owner_id	name
1	Alice
2	Bob

Vessele Table
vesseled_id	ve_name
1	Titan
2	Voyager


Vessele_owners (Junction Table)
id	vessele_id	owner_id
1	1	1
2	1	2
3	2	1


Vessel Titan (vesseled_id=1) is owned by Alice (owner_id=1) & Bob (owner_id=2).
Vessel Voyager (vesseled_id=2) is owned by Alice (owner_id=1).


Querying Data
1️⃣ Get all vessels owned by Alice

alice = Owner.objects.get(name="Alice")
print(alice.vessels.all())  # ✅ Returns all vessels owned by Alice


Generated SQL

SELECT vessele.*
FROM vessele
JOIN Vessele_owners ON vessele.vesseled_id = Vessele_owners.vessele_id
WHERE Vessele_owners.owner_id = 1;



2️⃣ Get all owners of a vessel of particular vessel
titan = Vessele.objects.get(ve_name="Titan")
print(titan.owners.all())  # ✅ Returns all owners of Titan



Generated SQL
SELECT owner.*
FROM owner
JOIN Vessele_owners ON owner.owner_id = Vessele_owners.owner_id
WHERE Vessele_owners.vessele_id = 1;



3️⃣ Assign a new owner to a vessel
vessel = Vessele.objects.get(ve_name="Voyager")
bob = Owner.objects.get(name="Bob")
vessel.owners.add(bob)  # ✅ Adds Bob as an owner of Voyager


4️⃣ Remove an owner from a vessel

vessel.owners.remove(bob)  # ✅ Removes Bob from ownership of Voyager


2️⃣ Reverse Foreign Key (related_name)
If a model has a ForeignKey, we can retrieve related objects in reverse using related_name.

Example: Vessel & Annual Analysis
One Vessel can have multiple Annual Analyses.
We want to retrieve all analyses for a vessel.
Django Models


class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)


SQL Equivalent

CREATE TABLE AnnualVesseleAnalysis (
    id SERIAL PRIMARY KEY,
    vessele_id INT REFERENCES Vessele(vesseled_id) ON DELETE CASCADE,
    plaenty VARCHAR(255),
    year INT
);


Data Representation
AnnualVesseleAnalysis Table

id	vessele_id	plaenty	year
1	1	Fine	2022
2	1	None	2023
3	2	Warning	2023

Vessel Titan (vesseled_id=1) has two analyses (Fine in 2022, No record in 2023).
Vessel Voyager (vesseled_id=2) has one analysis (Warning in 2023).


Querying Data
1️⃣ Get all annual reports for a vessel

vessel = Vessele.objects.get(ve_name="Titan")
print(vessel.annual_reports.all())  # ✅ Returns QuerySet of AnnualVesseleAnalysis


Generated SQL
SELECT *
FROM AnnualVesseleAnalysis
WHERE vessele_id = 1;


2️⃣ Get vessels that have NULL "plaenty" in their analysis
vessels = Vessele.objects.filter(annual_reports__plaenty__isnull=True)


Generated SQL
SELECT DISTINCT vessele.*
FROM vessele
JOIN AnnualVesseleAnalysis ON vessele.vesseled_id = AnnualVesseleAnalysis.vessele_id
WHERE AnnualVesseleAnalysis.plaenty IS NULL;

📌 Summary Table
Relationship	Field Type	SQL Behavior	Query Example
Many-to-Many	ManyToManyField	Creates a junction table	vessel.owners.all()
Reverse Foreign Key	ForeignKey(related_name="X")	Enables reverse lookup	vessel.annual_reports.all()

🚀 Final Thoughts
✅ Use ManyToManyField when two models need a bidirectional relationship.
✅ Use ForeignKey with related_name for efficient reverse lookups.
✅ Use select_related() & prefetch_related() for performance optimization.

1️⃣ Many-to-Many Relationship (ManyToManyField)
A record in Table A can be related to multiple records in Table B, and vice versa.

Example: Vessel & Owner
A Vessel can have multiple Owners.
An Owner can own multiple Vessels.
Django Models


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)
    owners = models.ManyToManyField(Owner, related_name="vessels")



Owner Table
owner_id	name
1	Alice
2	Bob
Vessele Table
vesseled_id	ve_name
1	Titan
2	Voyager
Vessele_owners (Junction Table)
id	vessele_id	owner_id
1	1	1
2	1	2
3	2	1



Query Outputs
1️⃣ Get all vessels owned by Alice

alice = Owner.objects.get(name="Alice")
print(alice.vessels.all())


Output
vesseled_id	ve_name
1	Titan
2	Voyager

2️⃣ Get all owners of a vessel

titan = Vessele.objects.get(ve_name="Titan")
print(titan.owners.all())


Output
owner_id	name
1	Alice
2	Bob

3️⃣ Assign a new owner to a vessel

vessel = Vessele.objects.get(ve_name="Voyager")
bob = Owner.objects.get(name="Bob")
vessel.owners.add(bob)



✅ Adds Bob as an owner of Voyager
Updated Vessele_owners Table:

id	vessele_id	owner_id
1	1	1
2	1	2
3	2	1
4	2	2


2️⃣ Reverse Foreign Key (related_name)
If a model has a ForeignKey, we can retrieve related objects in reverse using related_name.

Example: Vessel & Annual Analysis
One Vessel can have multiple Annual Analyses.
We want to retrieve all analyses for a vessel.


Django Models


class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)



Database Tables
AnnualVesseleAnalysis Table
id	vessele_id	plaenty	year
1	1	Fine	2022
2	1	None	2023
3	2	Warning	2023


Query Outputs
1️⃣ Get all annual reports for a vessel

vessel = Vessele.objects.get(ve_name="Titan")
print(vessel.annual_reports.all())


Output
id	vessele_id	plaenty	year
1	1	Fine	2022
2	1	None	2023


2️⃣ Get vessels that have NULL "plaenty" in their analysis
vessels = Vessele.objects.filter(annual_reports__plaenty__isnull=True)

Output
vesseled_id	ve_name
1	Titan



📌 Summary
Relationship	Field Type	SQL Behavior	Query Example	Output Table
Many-to-Many	ManyToManyField	Creates a junction table	vessel.owners.all()	Vessele_owners
Reverse Foreign Key	ForeignKey(related_name="X")	Enables reverse lookup	vessel.annual_reports.all()	AnnualVesseleAnalysis



✅ Use ManyToManyField when two models need a bidirectional relationship.
✅ Use ForeignKey with related_name for efficient reverse lookups.
✅ Use select_related() & prefetch_related() for performance optimization.



 Difference Between ForeignKey and Reverse Foreign Key in Django
 
 Feature	Foreign Key (ForeignKey)	Reverse Foreign Key (related_name)
Definition	A field in one model that creates a relationship to another model.	Allows retrieving related objects backward from the related model.
Direction	Defines a forward relationship from Model A to Model B.	Provides a reverse relationship from Model B back to Model A.
Where is it Defined?	Defined inside the model that holds the reference.	Accessed from the related model using related_name.
SQL Behavior	Adds a foreign key column in the referring table.	Enables querying the related objects without additional fields.
Query Example	analysis.vessele → Fetches the vessel from the analysis.	vessel.annual_reports.all() → Fetches all reports for a vessel.



📌 Example
We have two models:

Vessele (A vessel)
AnnualVesseleAnalysis (Stores yearly reports for vessels)



class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

class AnnualVesseleAnalysis(models.Model):
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    plaenty = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)



🔹 1️⃣ Foreign Key (Forward Lookup)
Scenario: Get the Vessele of a specific AnnualVesseleAnalysis report.

analysis = AnnualVesseleAnalysis.objects.get(id=1)
print(analysis.vessele.ve_name)  # Forward lookup


✅ Explanation:

vessele is a ForeignKey in AnnualVesseleAnalysis, so we can fetch the related Vessele directly.



🔹 2️⃣ Reverse Foreign Key (related_name)
Scenario: Get all AnnualVesseleAnalysis reports for a Vessel.


vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.annual_reports.all())  # Reverse lookup


✅ Explanation:

The related model (Vessele) doesn’t have a direct reference to AnnualVesseleAnalysis.
related_name="annual_reports" enables reverse lookup to fetch all AnnualVesseleAnalysis records.




📌 Summary
Use Case	ForeignKey (vessele)	Reverse Foreign Key (related_name)
Get Vessel from AnnualVesseleAnalysis	analysis.vessele	❌ Not needed
Get all Analyses for a Vessel	❌ Not possible	vessel.annual_reports.all()
✅ ForeignKey → Used for direct access to the related model.
✅ Reverse Foreign Key (related_name) → Used to fetch all related objects efficiently.



Example with Table Output for ForeignKey and Reverse ForeignKey (related_name)



📌 Data in Vessele Table


vesseled_id	ve_name
1	Titan
2	Ocean King



📌 Data in AnnualVesseleAnalysis Table


id	vessele_id (FK)	plaenty	year
1	1	Warning A	2020
2	1	Fine B	2021
3	2	Warning C	2019



🔹 1️⃣ Query Using ForeignKey (Forward Lookup)
Get the vessel name for AnnualVesseleAnalysis with id=1

analysis = AnnualVesseleAnalysis.objects.get(id=1)
print(analysis.vessele.ve_name)



✅ Output
Titan



Table Representation
Analysis ID	Vessel Name
1	Titan


🔹 2️⃣ Query Using Reverse Foreign Key (related_name)
Get all AnnualVesseleAnalysis records for Vessele with vesseled_id=1

vessel = Vessele.objects.get(vesseled_id=1)
print(vessel.annual_reports.all())


✅ Output

[AnnualVesseleAnalysis(id=1, plaenty='Warning A', year=2020),
 AnnualVesseleAnalysis(id=2, plaenty='Fine B', year=2021)]


Table Representation

Vessel Name	Analysis ID	Plaenty	Year
Titan	1	Warning A	2020
Titan	2	Fine B	2021

✅ Summary

Foreign Key (vessele) → Fetch one vessel from AnnualVesseleAnalysis.
Reverse Foreign Key (related_name="annual_reports") → Fetch all reports for a vessel



how to optimize both?
Optimizing Foreign Key and Reverse Foreign Key Queries in Django ORM
To improve performance, we can use select_related and prefetch_related to minimize the number of queries and optimize database access.


🔹 Optimizing ForeignKey Lookup (select_related)
🔻 Problem: N+1 Query Issue
If you retrieve AnnualVesseleAnalysis objects and access the related Vessele objects, Django will run an extra query for each foreign key lookup.

analysis_list = AnnualVesseleAnalysis.objects.all()

for analysis in analysis_list:
    print(analysis.vessele.ve_name)  # Causes extra queries (N+1 problem)


If there are 100 AnnualVesseleAnalysis records, this results in 1 query to fetch analyses + 100 extra queries to fetch related Vessele.


✅ Solution: Use select_related to Optimize Foreign Key Queries

analysis_list = AnnualVesseleAnalysis.objects.select_related('vessele').all()

for analysis in analysis_list:
    print(analysis.vessele.ve_name)  # No extra queries



🔹 How select_related Works
It performs a SQL JOIN between AnnualVesseleAnalysis and Vessele.
The Vessele data is fetched in the same query, reducing database hits.
Best for ForeignKey and OneToOneField (because they return a single related object).



🔹 Optimizing Reverse Foreign Key Lookup (prefetch_related)
🔻 Problem: Query Explosion for Reverse Foreign Key Lookup
If you fetch vessels and then access related AnnualVesseleAnalysis records, Django runs an extra query for each vessel.



vessels = Vessele.objects.all()

for vessel in vessels:
    print(vessel.annualvesseleanalysis.all())  # Causes multiple queries



If there are 100 vessels, and each has 5 related records, this results in 101 queries.

✅ Solution: Use prefetch_related for Reverse Foreign Key Optimization


vessels = Vessele.objects.prefetch_related('annualvesseleanalysis').all()

for vessel in vessels:
    print(vessel.annualvesseleanalysis.all())  # No extra queries



🔹 How prefetch_related Works
It performs two queries:
One to get all Vessele objects
Another to get all AnnualVesseleAnalysis objects related to those vessels
Django then matches them in Python, reducing the number of queries.
Best for ManyToManyField and Reverse ForeignKey (because they return multiple related objects).






🚀 Final Optimized Query
If you need both optimizations together, use both select_related and prefetch_related:
    
    
vessels = Vessele.objects.prefetch_related(
    'annualvesseleanalysis'
).select_related(
    'details'
)



select_related('details') → Optimizes the One-to-One relationship
prefetch_related('annualvesseleanalysis') → Optimizes the Reverse ForeignKey
✅ Now, only two queries are executed, making the retrieval faster and efficient. 



Django ORM (Query Methods & Symbols) - Beginner to Advanced Guide
Django ORM (Object-Relational Mapping) allows you to interact with the database using Python instead of writing raw SQL queries. 
Below is a complete guide covering different methods, symbols, and advanced querying techniques.



1️⃣ Creating Records (INSERT)
✅ Method 1: create()
Creates and saves a new record in a single step.

vessel = Vessele.objects.create(ve_name="Titanic")


✅ Method 2: save()
First, create an object, then call save() to store it in the database.

vessel = Vessele(ve_name="Queen Mary")
vessel.save()



✅ Method 3: bulk_create() (Multiple Inserts)
Inserts multiple objects efficiently.

vessels = [
    Vessele(ve_name="Voyager"),
    Vessele(ve_name="Ocean Pearl"),
]
Vessele.objects.bulk_create(vessels)



2️⃣ Retrieving Records (SELECT)
✅ Get a Single Record (get())


vessel = Vessele.objects.get(vesseled_id=1)



🔴 Raises DoesNotExist if no record is found.

✅ Get Multiple Records (filter())

vessels = Vessele.objects.filter(ve_name="Titanic")  # Returns QuerySet


✅ Get All Records (all())

vessels = Vessele.objects.all()


✅ Get the First & Last Record (first(), last())

first_vessel = Vessele.objects.first()
last_vessel = Vessele.objects.last()


✅ Get a Random Record (order_by('?'))

random_vessel = Vessele.objects.order_by('?').first()


3️⃣ Filtering Records (WHERE Clause)
Django uses symbols (__) for advanced filtering.

✅ Equals (=)



Vessele.objects.filter(ve_name="Titanic")


✅ Not Equal (exclude())
Vessele.objects.exclude(ve_name="Titanic")



✅ Greater Than / Less Than (__gt, __lt, __gte, __lte)

AnnualVesseleAnalysis.objects.filter(year__gt=2000)  # year > 2000
AnnualVesseleAnalysis.objects.filter(year__lte=1990)  # year <= 1990


✅ Contains (__icontains) → Case-insensitive

Vessele.objects.filter(ve_name__icontains="titanic")  # Matches "Titanic", "TitanicX"


✅ Starts / Ends With (__startswith, __endswith)

Vessele.objects.filter(ve_name__startswith="T")  # Starts with "T"
Vessele.objects.filter(ve_name__endswith="ic")  # Ends with "ic"


✅ IN Query (__in)
Vessele.objects.filter(ve_name__in=["Titanic", "Queen Mary"])



✅ NULL Values (__isnull)
AnnualVesseleAnalysis.objects.filter(plaenty__isnull=True)



4️⃣ Query Operators (Q, F)
✅ Using Q (OR Queries)

from django.db.models import Q

Vessele.objects.filter(Q(ve_name="Titanic") | Q(ve_name="Queen Mary"))


✅ Using F (Comparing Fields)
from django.db.models import F

AnnualVesseleAnalysis.objects.filter(year__gt=F('vesseled_id'))


5️⃣ Updating Records (UPDATE)
✅ Updating a Single Record

vessel = Vessele.objects.get(vesseled_id=1)
vessel.ve_name = "Titanic Updated"
vessel.save()


✅ Bulk Update

Vessele.objects.filter(ve_name="Titanic").update(ve_name="Titanic 2.0")


6️⃣ Deleting Records (DELETE)
✅ Delete a Single Record

vessel = Vessele.objects.get(vesseled_id=1)
vessel.delete()


✅ Bulk Delete
Vessele.objects.filter(ve_name="Titanic").delete()



7️⃣ Ordering & Limiting Results
✅ Order By Ascending / Descending
Vessele.objects.order_by('ve_name')  # Ascending
Vessele.objects.order_by('-ve_name')  # Descending


✅ Limit Results ([:N])
Vessele.objects.all()[:10]  # Get first 10 results



8️⃣ Aggregation & Annotation
✅ Count, Sum, Avg, Min, Max

from django.db.models import Count, Sum, Avg, Min, Max

Vessele.objects.aggregate(Count('vesseled_id'))  # Count total vessels
AnnualVesseleAnalysis.objects.aggregate(Avg('year'))  # Average year


✅ Annotate (Field Computation)
Vessele.objects.annotate(num_entries=Count('annualvesseleanalysis'))



9️⃣ Advanced Querying
✅ select_related() (ForeignKey Optimization)
AnnualVesseleAnalysis.objects.select_related('vessele').all()


✅ prefetch_related() (Reverse ForeignKey Optimization)
Vessele.objects.prefetch_related('annualvesseleanalysis').all()


🔟 Many-to-Many Queries
✅ Example: Models

class Captain(models.Model):
    name = models.CharField(max_length=100)

class Ship(models.Model):
    name = models.CharField(max_length=100)
    captains = models.ManyToManyField(Captain, related_name="ships")

✅ Adding Many-to-Many Relationships
captain = Captain.objects.create(name="John")
ship = Ship.objects.create(name="Titanic")

ship.captains.add(captain)  # Assign Captain to Ship


✅ Querying Many-to-Many Relationships
Captain.objects.filter(ships__name="Titanic")


🔟 Reverse Foreign Key Queries
✅ Get all AnnualVesseleAnalysis linked to a Vessele

vessel = Vessele.objects.get(vesseled_id=1)
analysis = vessel.annualvesseleanalysis.all()


🚀 Final Summary (Symbols & Queries)
Symbol / Method                          	Usage Example	                                                     Explanation
=	                                    filter(ve_name="Titanic")	                                                  Exact match
__gt, __lt	                                filter(year__gt=2000)	                                              Greater/Less than
__icontains                         	filter(ve_name__icontains="titanic")	                           Case-insensitive contains
__startswith, __endswith	                    filter(ve_name__startswith="T")	                              Starts/Ends with
__in	                                                filter(ve_name__in=["Titanic", "Queen Mary"])	 Matches values in list
__isnull	                            filter(plaenty__isnull=True)	                             Check for NULL values
Q	                               `filter(Q(ve_name="Titanic")                             	Q(ve_name="Queen Mary"))`
F	                                     filter(year__gt=F('vesseled_id'))                            	Compare fields
select_related()	select_related('vessele')	                                                     Optimize ForeignKey
prefetch_related()	prefetch_related('annualvesseleanalysis')	                                      Optimize Reverse ForeignKey




📌 Django ORM Queries Explained with Tables
🛠 Models


class Vessele(models.Model):
    vesseled_id = models.AutoField(primary_key=True)
    ve_name = models.CharField(max_length=255)

class AnnualVesseleAnalysis(models.Model):
    analysis_id = models.AutoField(primary_key=True)
    vessele = models.ForeignKey(Vessele, on_delete=models.CASCADE, related_name="annual_reports")
    year = models.IntegerField()
    revenue = models.FloatField()


1️⃣ INSERT Data
✅ Using .create()

vessel = Vessele.objects.create(ve_name="Titanic")


📌 Table Output (Vessele table after insertion)
vesseled_id	ve_name
1	Titanic

🔹 Return Type:

create() returns a model instance → <Vessele: Titanic>


2️⃣ SELECT Data
✅ .all() (Get All Rows)
Vessele.objects.all()



📌 Output (Vessele table)

vesseled_id	ve_name
1	Titanic
2	Queen Mary
3	Voyager


🔹 Return Type:

QuerySet → <QuerySet [<Vessele: Titanic>, <Vessele: Queen Mary>, <Vessele: Voyager>]>

✅ .filter() (WHERE Condition)

Vessele.objects.filter(ve_name="Titanic")

📌 Output: Matching Rows

vesseled_id	ve_name
1	Titanic
🔹 Return Type:

QuerySet → <QuerySet [<Vessele: Titanic>]>

✅ .get() (Get a Single Object)

Vessele.objects.get(vesseled_id=1)


📌 Output

vesseled_id	ve_name
1	Titanic
🔹 Return Type:

Model Instance → <Vessele: Titanic>
❌ If multiple results or no results → DoesNotExist or MultipleObjectsReturned error.


3️⃣ UPDATE Data
✅ .update() (Bulk Update)

Vessele.objects.filter(ve_name="Titanic").update(ve_name="Titanic 2.0")


📌 Output (Vessele table after update)

vesseled_id	ve_name
1	Titanic 2.0
2	Queen Mary
🔹 Return Type:

Integer (number of updated rows) → 1


4️⃣ DELETE Data
✅ .delete()

Vessele.objects.filter(ve_name="Titanic 2.0").delete()

📌 Output (Vessele table after deletion)

vesseled_id	ve_name
2	Queen Mary
🔹 Return Type:

Tuple → (Number of deleted rows, {'app_name.ModelName': count})
Example: (1, {'app.Vessele': 1})


5️⃣ Foreign Key & Reverse Foreign Key Queries
📌 Example Data (AnnualVesseleAnalysis table)
analysis_id	vessele_id	year	revenue
1	1	2010	5.5M
2	1	2015	7.8M
3	2	2018	6.2M


✅ Forward ForeignKey (select_related())

analysis = AnnualVesseleAnalysis.objects.select_related("vessele").get(analysis_id=1)
print(analysis.vessele.ve_name)


📌 Output:
🚀 Optimized Query (Single SQL JOIN)

Titanic



🔹 Return Type:

Model Instance (<AnnualVesseleAnalysis: 2010 Report>)


✅ Reverse ForeignKey (prefetch_related())

vessel = Vessele.objects.prefetch_related("annual_reports").get(vesseled_id=1)
print(vessel.annual_reports.all())


📌 Output:

analysis_id	vessele_id	year	revenue
1	1	2010	5.5M
2	1	2015	7.8M


🔹 Return Type:

QuerySet → <QuerySet [<AnnualVesseleAnalysis: 2010 Report>, <AnnualVesseleAnalysis: 2015 Report>]>



6️⃣ Many-to-Many Relationships
📌 Example Models


class Captain(models.Model):
    name = models.CharField(max_length=100)

class Ship(models.Model):
    name = models.CharField(max_length=100)
    captains = models.ManyToManyField(Captain, related_name="ships")



✅ Assign Captains to Ships

captain = Captain.objects.create(name="John")
ship = Ship.objects.create(name="Titanic")

ship.captains.add(captain)



📌 Output (Ship_Captains Many-to-Many Join Table)


id	ship_id	captain_id
1	1	1


✅ Querying Many-to-Many Data

Captain.objects.filter(ships__name="Titanic")



📌 Output (All Captains of Titanic)


id	name
1	John
🔹 Return Type:

QuerySet → <QuerySet [<Captain: John>]>


🔍 Summary Table of Django Query Methods
Operation	Query Example	Return Type
Insert	create(ve_name="Titanic")	Model Instance
Select	all()	QuerySet
Filter	filter(ve_name="Titanic")	QuerySet
Get	get(vesseled_id=1)	Model Instance
Update	update(ve_name="Titanic 2.0")	Integer (Rows Updated)
Delete	delete()	Tuple (Rows Deleted, {Model: Count})
ForeignKey Forward	select_related("vessele")	Model Instance
Reverse ForeignKey	prefetch_related("annual_reports")	QuerySet
Many-to-Many Add	ship.captains.add(captain)	None
Many-to-Many Query	filter(ships__name="Titanic")	QuerySet
🚀 Final Notes
Use select_related() for ForeignKey to reduce queries.
Use prefetch_related() for Reverse ForeignKey & Many-to-Many to optimize performance.
Use bulk_create() for batch inserts.
































    



