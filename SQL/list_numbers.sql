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

--list of perfect numbers up to :p_number
SELECT LISTAGG(a,'.') WITHIN GROUP (ORDER BY a) PERFECT_LIST
FROM
(
SELECT a
    , (SELECT SUM(c) DSUM FROM (SELECT LEVEL c FROM DUAL CONNECT BY LEVEL<a) WHERE a/c = TRUNC(a/c)) DSUM
FROM
(
SELECT LEVEL a FROM DUAL CONNECT BY LEVEL<=:p_number
)
)
WHERE a = DSUM
AND a>1
/
