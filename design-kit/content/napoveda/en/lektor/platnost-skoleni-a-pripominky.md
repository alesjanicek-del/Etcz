---
title: Training validity and renewal reminders
source: https://demo.exam-test.cz/napoveda/lektor/platnost-skoleni-a-pripominky
translation: unofficial-draft
---

Who has a valid certificate, whose certificate expires soon and whose has expired. XLSX export and email reminders before expiry.

You can follow tests that issue certificates with limited validity in the **Training validity** overview. Before a certificate expires, the application sends an email reminder.

## The Training validity overview

Open **Evaluation → Training validity**.

- For each person and test, the latest passed certificate counts. If a person retakes and passes the test again, the new date applies.
- The status is **valid**, **expires soon** (validity ends sooner than the first reminder is due; 30 days by default) or **expired**.
- Filter by test, branch and status, then select **Filter**.
- **Export validity (XLSX)** downloads a table for the current filter.

Who sees what is the same as for results. Instructors see people from the assignments they created, branch administrators see their branch, and organisation administrators see everyone.

## Who is missing from the overview and reminders

The application does not yet keep a permanent register of people across exams. So it links one person’s attempts only:

- by user account (learners with an assigned test, **My tests**),
- by the email on an access code (codes sent by email).

Attempts from codes without an email, from links and from supervised in-room exams cannot be reliably matched to the same person. They are not included in the overview or reminders. The overview states how many there are, and you can find their certificates in **Results**. If you want to track validity, assign repeat training to learners or with codes that have an email.

## Email reminders

The settings are in **Administration → Organisation settings → Training renewal reminders**:

- **Send certificate expiry reminders**: turns all reminders on or off.
- **Days before expiry to send a reminder**: “30, 7” by default. Leave empty to send only a reminder after expiry.
- **Also remind after expiry**: once, no later than 30 days after expiry.
- **Who gets the reminder summary**: the instructor who created the test assignment (or organisation administrators, if that instructor no longer has an active account), organisation administrators, or nobody.

How reminders are sent:

- The application checks once a day, in the morning.
- The test taker gets an email at their account address or at the email on their access code. The summary recipient (instructor or organisation administrator) gets one summary a day with a list of people.
- Each reminder is sent only once. The application keeps track of reminders it has sent, so a repeated check does not send a duplicate email. If the check does not run one day, only the most urgent reminder is sent.
- A short-lived certificate does not get a reminder straight after it is issued. For example, with a one-month validity, only the reminder 7 days before expiry is sent.
- Reminders need the application to have email sending set up. If it does not, the **Organisation settings** page tells you.

Email reminders to employees are processing of personal data by your organisation as the data controller. For employees, they usually rely on the employer’s duty to provide repeat training. The default privacy information for test takers mentions reminders, certificates and the longer retention of attempts with a valid certificate. If you use your own privacy text in **Organisation settings**, add this information to it.

The reminder summary contains test takers’ names. Send it only to the people who organise repeat training.

## Retention period and certificate validity

The results retention period (**Organisation settings → Data and texts**) can be shorter than a certificate’s validity. So that a certificate does not lose its holder’s name before it expires, the application anonymises an attempt with a valid certificate only 30 days after the certificate expires. Certificates with no expiry do not delay anonymisation. **Organisation settings** warns you about such a difference and shows how many attempts are being kept for this reason.

Manual anonymisation of a person at their request is not restricted. The certificate can then no longer be downloaded.

*For roles: Instructor, Branch administrator, Organisation administrator*
