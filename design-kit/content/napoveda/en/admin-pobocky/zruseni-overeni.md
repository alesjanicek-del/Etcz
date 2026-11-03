---
title: Resetting two-step verification
source: https://demo.exam-test.cz/napoveda/admin-pobocky/zruseni-overeni
translation: unofficial-draft
---

When a user has lost both their phone and their backup codes. Verify their identity first.

## Steps

1. Verify the requester’s identity, for example by calling a number you know. Never reset verification based on an email alone.
2. Go to **Administration** → **Users** and open the user’s details.
3. In **Reset two-step verification**, fill in **Reason (required)**.
4. Click **Reset verification** and confirm.

Branch administrators can reset verification only for users whose roles are all in branches they manage. For question authors and users with a role in another branch, the organisation administrator does it. The reason must be at least 5 characters long.

## What happens next

- The user is signed out and receives an email.
- They set up verification again the next time they sign in.
- The action is recorded in the change log.

If the user still has a backup code, they do not need a reset. They can sign in with the backup code and set up verification again themselves (see [Two-step verification](../zaciname/overeni-ve-dvou-krocich.md)).

*For roles: Branch administrator, Organisation administrator*
