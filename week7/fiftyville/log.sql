-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Firstly, inspected crime scene reports for 28 July, 2021 at Humphrey Street.
SELECT *
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = "Humphrey Street";

-- Inspect interviews for this date using keyword "bakery", as it was mentioned in transcript, according to 'description' from 'crime_scene_reports':
SELECT *
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE "%bakery%";

-- Searching for camera logs, according to the first transcript
SELECT *
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minutes > 15
AND minutes < 25
AND activity = "exit";

-- Searching for atm logs, according to the second transcript:
SELECT *
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND activity = "withdraw"
AND atm_location LIKE "%Leggett%";

-- Searching for phone logs (3rd transcript):
SELECT *
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Searching data of all people who withdrawed money at Leggett Street:
SELECT *
FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN
    (SELECT account_number
    FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND transaction_type = "withdraw"
    AND atm_location LIKE "%Leggett%");



-- Selected names of people, who withdrawed money on 28.07.2021, left bakery inbetween 10:15 and 10:25,
--spoke on the phone this day less than 60 seconds, bought flight tickets for 29.07.2022.
SELECT name
FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND transaction_type = "withdraw"
    AND atm_location LIKE "%Leggett%"
)
AND license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute > 15
    AND minute < 25
    AND activity = "exit"
)
AND phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
)
AND passport_number IN (
    SELECT passport_number
    FROM passengers JOIN flights on passengers.flight_id = flights.id
    WHERE year = 2021
    AND month = 7
    AND day = 29
);
-- Query outputs two names - Bruce and Diana. Since in interview was told,
-- that conjective suspect bought the EARLIEST ticket from Fiftyville, we can conclude,
-- That Bruce is obvious suspect. His flight is scheduled at 08:20, whereas Diana's flight - at 16:00.


-- Selecting name of person, who spoke with Bruce.
SELECT name
FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE caller = "(367) 555-5533"
    AND year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
);
-- Outputs Robin.

-- Selecting city Bruce escaped to:
SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE id = (
        SELECT flight_id FROM passengers WHERE passport_number = (
            SELECT passport_number
            FROM people
            WHERE name = "Bruce")
));
-- Outputs New York City.




