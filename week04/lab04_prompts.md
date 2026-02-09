# Lab 04 – AI Prompts and Responses

## Problem 1: Finding Common Items

**Prompt used:**

I have two very large Python lists of product IDs. I need to find which items appear in both lists. The order of the final result does not matter, but performance is important. What Python data structure should I use and why?

**AI Recommendation and Reasoning:**

The best data structure for this problem is a **set**. Sets automatically remove duplicates and allow very fast membership testing and intersection operations. By converting both lists into sets and using set intersection, the common elements can be found efficiently, even for very large datasets.



## Problem 2: User Profile Lookup

**Prompt used:**

I have a list of user profiles, where each user is represented as a dictionary with name, age, and email. I regularly need to look up a user's full profile by their username, and performance is critical. What Python data structure should I use?

**AI Recommendation and Reasoning:**

A **dictionary** is the most efficient data structure for this use case. Dictionaries allow constant-time (O(1)) lookups using a key. By converting the list of users into a dictionary where the username is the key and the user profile is the value, user profiles can be retrieved very quickly.



## Problem 3: Listing Even Numbers in Order

**Prompt used:**

I have a list of integers and need to create a new list that contains only the even numbers, while preserving the original order. What Python approach or data structure should I use?

**AI Recommendation and Reasoning:**

A **list** is the best choice because order matters. A list comprehension is an efficient and readable way to iterate through the list, filter out odd numbers, and preserve the original order of the even numbers.
