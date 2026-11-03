---
title: Sign-in with an email link
source: https://demo.exam-test.cz/napoveda/admin-organizace/prihlaseni-odkazem
translation: unofficial-draft
---

Users can sign in with a one-time link sent by email instead of a password. This feature is off by default.

## What the feature does

Once it is on, your organisation’s sign-in page offers **Email me a sign-in link**. The user enters their email address and receives a link to sign in without a password.

- The link is valid for **15 minutes** and can be used **only once**.
- The link replaces the password, **not two-step verification**. Users with verification turned on or required still enter the code from their phone after opening the link, just as after entering a password.
- The link works only for your organisation. It cannot be used to sign in to another organisation.
- The link stops working after a password change, after signing out on all devices and after any other sign-in.
- Only active accounts that already have a password receive a link. Newly invited users must accept their invitation first.
- The response to a request is always the same, even if the account does not exist. Nobody can use it to find out who has an account with you.
- Both issuing a link and signing in with it are recorded in the change log. The link itself is not stored anywhere.

## How to turn it on

1. Open **Administration** → **Organisation settings**.
2. In **Sign-in**, tick **Allow sign-in with an email link**.
3. Click **Save settings**.

The change is recorded in the change log. To turn the feature off, follow the same steps. Links that have already been sent stop working once it is off.

The app operator can also turn the feature on or off at your request. You receive an email, and the change appears in your organisation’s change log with a reason.

## When not to turn on email link sign-in

With email link sign-in, account security depends on the security of the mailbox. Anyone who gets into a user’s mailbox can sign in as that user.

- **Official exams:** keep the feature off, or turn it on only together with **Require two-step verification for instructors too**. Verification is always required for administrators and authors.
- **Shared mailboxes:** if instructors use a shared department mailbox, do not turn the feature on.
- If email is not working, the link does not arrive. Users can still sign in with their password as before.

*For roles: Organisation administrator*
