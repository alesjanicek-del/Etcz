---
title: Results, result reports and releasing results
source: https://demo.exam-test.cz/napoveda/lektor/vysledky-a-protokol
translation: unofficial-draft
---

Results by role and branch, attempt details with an activity record, PDF result report, releasing results and XLSX export.

## Who sees which results

Open **Evaluation → Results**.

- An **instructor** sees results of the assignments they created themselves: in branches where they have the instructor role, and assignments without a branch.
- A **branch administrator** sees results from all the branches they manage.
- An **organisation administrator** sees all results, including assignments without a branch.

The active branch in the top bar does not filter results. If you have a role in several branches, you see results from all of them at once. To see one branch, use the **Branch** filter. The active branch only decides where new assignments are created and which batches **Print** shows.

To see results for a single assignment, select **Results** in its details.

## Filter and export

- Filter by test, branch, date, result (**Passed** / **Not passed**) and name. Select **Filter**.
- **Export results (XLSX)** downloads a table for the current filter: test taker, test, method, branch, test version, times, points, percentage, result, grade and verification code.
- Organisation administrators also see **Branch comparison** (number of people, number of attempts, average, pass rate). They can download it with **Export branch comparison (XLSX)**.
- For results of link assignments, there is a **Compare links** button. It compares each link’s started and submitted attempts, average, median, pass rate and average time.
- When you filter by one test (or open an assignment’s results), the **Training record (PDF)** and **Training record (XLSX)** buttons appear. See [Certificates and training records](osvedceni-a-zaznam-o-skoleni.md). You can download the certificate for a single attempt in the result details.

## Views by assignment method

- **Supervised in-room exams** show results for each exam held in the room.
- **Assigned tests** show, for each learner and group, who has passed, not passed or not yet started the test.
- **Training validity** shows who has a valid certificate and whose certificate expires soon (see [Training validity and refresher reminders](platnost-skoleni-a-pripominky.md)).

## Attempt details

Select the test taker’s name. The details include:

- **Evaluation**: percentage, points, result (Passed or Not passed), start and submission time, and who submitted (test taker, time-out, instructor, paper entry, automatically by monitoring), extra time,
- **Verification code** and the record’s verification status,
- **Questions and answers** in the order of the test version, with the question version, chosen and correct answers, and points,
- **Test activity (record)**: a timeline of events (start, questions shown, answer changes, leaving the window, extra time, submission). Events recorded offline (during a connection outage) arrive only once the connection is back. They are placed by the time on the test taker’s device, which is shown next to them.

Details for specialists (checksums) are in the collapsed **Technical details** section.

## Result report (PDF)

In the attempt details, select **Result report (PDF)**. The result report contains the organisation’s logo and details, the time limit and extra time, all questions and answers, and the result. It also has the activity record, the verification code and a QR code for checking authenticity (see [Verifying a result report](../zkouseni/overeni-protokolu.md)).

Test takers can only download a test taker’s summary. It has the same verification code. But it shows questions only as far as the test’s results display setting allows (never with correct answers for an official test). The summary is marked as such in its header. So for the file (for example, as an annex to the official exam minutes), keep the result report downloaded here, in the attempt details.

Every result report download is recorded in the change log.

## Releasing results

If **Show result only after the instructor releases it** is on for the test:

1. In the results list, tick the attempts.
2. Select **Release selected results to test takers**.

The **Released** column shows the release date, or “no”. Learners see their result under **My results**.

## Personal data

The organisation administrator protects records, anonymises data and exports data (see Personal data, anonymisation and data export).

*For roles: Instructor, Branch administrator, Organisation administrator*
