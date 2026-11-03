---
title: Organisation settings
source: https://demo.exam-test.cz/napoveda/admin-organizace/nastaveni-organizace
translation: unofficial-draft
---

Name and logo, processes (approval, two-step verification, links), test defaults, retention period, texts for test takers and accessibility statement details.

Open **Administration** → **Organisation settings**. Click **Save settings** to save your changes. Every change is recorded in the change log. The **Details** column shows what changed, from which value to which. Long texts are shortened in the change log. Email addresses are shortened to the first letter and the domain.

## Organisation

- **Organisation name**: shown in the app, on result reports and in printouts.
- **Contact email**.
- **Logo**: PNG, JPEG or WebP, up to 2 MB. Shown in the app, on the result report and in print.

## Processes and permissions

- **Question approval**: only the approved version of a question goes into tests (see [Question approval](../autor/schvalovani-otazek.md)).
- **Branch administrators can also approve questions**.
- **Require two-step verification for instructors too**. It is always required for administrators and question authors. It is also required for instructors who own or can edit a question bank or a test.
- **Instructors can create question banks** and **Instructors can create tests**.
- **Allow test assignment by public link (anonymous testing)**. Turning this off blocks new links.

## Sign-in

- **Allow sign-in with an email link**: users can sign in with a one-time link instead of a password. Off by default. To find out when to turn it on, see [Sign-in with an email link](prihlaseni-odkazem.md).

## Defaults for new tests

**Time limit (minutes)**, **Maximum attempts**, **Visible to test taker after submission**, **Answer feedback** and more. Instructors can change them for each test.

## Refresher training reminders

**Send certificate expiry reminders**, **Days before expiry to send reminders** (default “30, 7”), **Also remind after expiry** and **Send reminder summary to**. For details, see [Training validity and refresher reminders](../lektor/platnost-skoleni-a-pripominky.md).

## Data and texts

- **Result retention period (months)**: after this period, test takers’ personal data is anonymised. Result reports can still be verified. The default is 60 months. An attempt with a valid certificate is anonymised only 30 days after the certificate expires.
- **Introductory text before the test**: test takers see it on the test’s start page.
- **Result report footer**.
- **Privacy notice**: test takers open it from a link on the test’s start page. If you leave it empty, the app uses a default text with your organisation’s contact and the retention period.

## Accessibility statement

Details for the [accessibility statement](/prohlaseni-o-pristupnosti) shown at your organisation’s address:

- **We are a public sector body under Act No. 99/2019 Coll., on Accessibility**: tick this if your organisation is a public authority, municipality, region, school or other public body. You then issue the statement as your own. It names the Ministry of the Interior as the supervisory body. This is ticked in advance for the Veřejná správa (Public Administration) plan. If you leave it unticked, the statement says you issue it voluntarily.
- **Date the statement was prepared or approved**: the date you reviewed and approved the statement. If you leave it empty, the statement shows the date the app operator prepared the draft.
- **Link to the statement or organisation website**: the address where you publish the statement on your website.
- **Accessibility feedback email**: if you leave it empty, the app uses the **Contact email**.

The app operator fills in the list of the app’s accessibility issues and how they will be fixed.

## Support access

See [Support technician access](pristup-podpory.md).

*For roles: Organisation administrator*
