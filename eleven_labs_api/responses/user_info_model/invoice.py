from dataclasses import dataclass


@dataclass
class Invoice:
    amount_due_cents: int
    next_payment_attempt_unix: int
