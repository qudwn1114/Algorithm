SELECT HOUR(DATETIME) as HOUR, COUNT(*) as COUNT FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 and 19
GROUP BY HOUR
ORDER BY HOUR;

# alias where 절에서 사용 불가능!!!!