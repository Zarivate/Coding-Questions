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
# overlap. In other words, the goal is to find the maximum pay possible on each specific day and add them up to get your 
# overall max pay. This can be done through either sorting the array beforehand or iterating through the array multiple
# times for each day. In otherwords iterating at most 7 days, as that is how many days are in a week.



# Implementation:
def optimalFreelance(jobs):
    # 7 days in a week
    daysLeft = 7
    # Variable to hold the total pay
    totalPay = 0
    # While loop that at most will iterate 7 times 
    while daysLeft > 0:
        # Variable to hold the maximum amount of payment on the day
        maxDayPay = 0
        # Position of the job in the jobs array
        jobIdx = None
        # Iterate through every job in the jobs array, while keeping track of their positions
        for idx, job in enumerate(jobs):
            # If job is found that is greater than the number of daysLeft to work in the week, in otherwords a job
            # that has a deadline capable of being done within any day on and before the daysLeft, and the payment is
            # greater than the previously found maxPayment of another job
            if job["deadline"] >= daysLeft and job["payment"] > maxDayPay:
                # Set the maxDayPay variable equal to that job's payment
                maxDayPay = job["payment"]
                # Store the idx
                jobIdx = idx

        # If the pay is greater than 0
        if maxDayPay != 0:
            # Add it to the total
            totalPay += maxDayPay
            # Remove the job from the jobs array to shorten iteration
            jobs.pop(jobIdx)
        # Decrement the possible days able to work
        daysLeft -= 1
    return totalPay


# In depth breakdown:
example_jobs3 = [
    {"deadline": 1, "payment": 1}, # 0
    {"deadline": 2, "payment": 1}, # 1
    {"deadline": 5, "payment": 1}, # 2
    {"deadline": 6, "payment": 2}, # 3 
    {"deadline": 7, "payment": 3}, # 4 
]

# daysLeft = 7
# totalPay = 0
# Enter outer while loop
# maxDayPay = 0
# jobIdx = 0
# Enter inner for loop

# At first job,
# jobs[0] = deadline: 1, payment: 1
# deadline: 1 < 7, payment: 1 > 0
# Payment is greater than maxDayPay but deadline is less than the number of days left. Meaning it's not optimal to do this
# job right now so move onto next job

# jobs[1] = deadline: 2, payment: 1
# deadline: 2 < 7, payment: 1 > 0
# Payment is greater than maxDayPay but deadline is less than the number of days left. Meaning it's not optimal to do this
# job right now so move onto next job

# jobs[2] = deadline: 5, payment: 1
# deadline: 5 < 7, payment: 1 > 0
# Payment is greater than maxDayPay but deadline is less than the number of days left. Meaning it's not optimal to do this
# job right now so move onto next job

# jobs[3] = deadline: 6, payment: 2
# deadline: 6 < 7, payment: 2 > 0
# Payment is greater than maxDayPay but deadline is less than the number of days left. Meaning it's not optimal to do this
# job right now so move onto next job

# jobs[4] = deadline: 7, payment: 3
# deadline: 7 <= 7, payment: 3 > 0
# Both deadline and payment match conditions, so variables can be overwritten with their variables
# maxDayPay = 3
# jobIdx = 4

# Exit out of for loop now and check if condition
# maxDayPay = 3, 3 != 0 so enter if check
# Add totalPay and remove job from jobs array
# totalPay += 3
# jobs.pop(4)

# totalPay = 3
# example_jobs3 = [
#     {"deadline": 1, "payment": 1}, # 0
#     {"deadline": 2, "payment": 1}, # 1
#     {"deadline": 5, "payment": 1}, # 2
#     {"deadline": 6, "payment": 2}, # 3 
# ]
# Decrement daysLeft as now there is 1 less day able to be worked on
# daysLeft -= 1, daysLeft = 6
# Repeat process to find can do all jobs for a totalPay of 8

print(optimalFreelance(example_jobs3))
