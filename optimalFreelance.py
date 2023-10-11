# Question:

# Given a freelance software development job, where each job has a deadline and payment, write a function that 
# returns the maximum payment possible within a 7 day time period.

# Note:
# After a deadline there is no value in completing the work, meaning the work must be done on time
# Only 1 job can be done at a time
# Each job takes 1 full day to complete
# Deadline will be given as the number of days left to do the job, 
#   IE: A job of deadline 1 can only be done if it's the first job worked on, 
#       a deadline of 2 means it can be started on the first or second day, as each job takes 1 day to do so can be worked on a day
#       after a previous job is done. As that would leave the deadline to go down by 1, menaing there would still be a day left to do it.
# Sometimes it won't be possible to do all the jobs
# There's no requirement to do all the jobs

# Example:
example_jobs = [
    {"deadline": 1, "payment": 1}, # Means there is 1 day left to do this job and will pay you 1
    {"deadline": 2, "payment": 1}, # Means there is 2 days left to do this job and will pay you 1
    {"deadline": 2, "payment": 2}  # Means there is 2 days left to do this job and will pay you 2
]


# Answer
# 3
# Job 0 is done first, then job 2 as that has a higher payment than job 1, and job 1 would be skipped

# Optimal Space and Time Complexity:
# O(1) space
# O(n) time
# n = length of jobs object/number of jobs available

# Explanation:
# An important thing to realize for this problem is how the highest payment possible will require properly
# spacing out the days you work so the jobs with longer deadlines are done last, so there is more time to do
# others jobs before those. IE:

example_jobs2 = [
    {"deadline": 1, "payment": 1}, # 0
    {"deadline": 2, "payment": 1}, # 1
    {"deadline": 2, "payment": 2}, # 2
    {"deadline": 3, "payment": 2}, # 3 
    {"deadline": 4, "payment": 1}, # 4 
    {"deadline": 5, "payment": 3}, # 5 
    {"deadline": 5, "payment": 1}, # 6 
]

# There are two jobs with a deadline in 5 days, but only 1 of them has a payment of 3 while the other has a payment of 1.
# Optimally, the job with a payment of 3 should be done instead but preferably on the 5th day. That way, the 4 days before 
# that other jobs can be done. Following the same pattern of choosing the higher paying jobs for any days where the deadlines
# overlap. In other words, the goal is to find the maximum pay possible on each specific day and add them up to det your 
# overall max pay. This can be done through either sorting the array beforehand or iterating through the array multiple
# times for each day. In otherwords iterating at most 7 days, as that is how many days are in a week.

# Implementation:

