--list divisors of :p_number seperated by a '.'
SELECT LISTAGG(a,'.') WITHIN GROUP (ORDER BY a DESC) DIVISORS
FROM
(
SELECT LEVEL a FROM DUAL CONNECT BY LEVEL <= :p_number)
WHERE :p_number/a = TRUNC(:p_number/a);
/

--calculate the divisor sum of :p_number
SELECT SUM(a) DIVISOR_SUM
FROM
(
SELECT LEVEL a FROM DUAL CONNECT BY LEVEL < :p_number)
WHERE :p_number/a = TRUNC(:p_number/a)
/