#!/usr/bin/env python

import unicodecsv
enrollments_filename = 'enrollments.csv'
engagement_filename = 'daily_engagement.csv'
submissions_filename = 'project_submissions.csv'

def reader():
    with open(enrollments_filename, 'rb') as enrollf:
        ereader = unicodecsv.DictReader(enrollf)
        enrollments = list(ereader)
    idList = []
    for row in enrollments:
        idList.append(row['account_key'])
    enrollment_num_rows = len(enrollments)# Replace this with your code
    enrollment_num_unique_students = len(set(idList))  # Replace this with your code

    idList = []
    with open(engagement_filename, 'rb') as engagef:
        enreader = unicodecsv.DictReader(engagef)
        daily_engagement = list(enreader)
    for row in daily_engagement:
        row['account_key'] = row['acct']
        del row['acct']
        idList.append(row['account_key'])

    engagement_num_rows = len(daily_engagement)
    engagement_num_unique_students = len(set(idList))

    idList = []
    with open(submissions_filename, 'rb') as subf:
        preader = unicodecsv.DictReader(subf)
        project_submissions = list(preader)
    for row in project_submissions:
        idList.append(row['account_key'])

    submission_num_rows = len(project_submissions)            # Replace this with your code
    submission_num_unique_students = len(set(idList))
     
    print submission_num_unique_students
    print submission_num_rows

    print engagement_num_unique_students
    print engagement_num_rows

    print enrollment_num_unique_students
    print enrollment_num_rows
reader()
