# Put all the following files in the same directory
# make_pomdp_file.py
# pomdpsol
# pomdpeval

mkdir newstuff

python3 make_pomdp_file.py
# here enter your roll number and question number 0,1,2,3 respectively


# after the above step, copy paste all these files
./pomdpsol --output newstuff/2018111040_0.policy  newstuff/2018111040_0.pomdp > newstuff/2018111040_0.out
echo "First done"
./pomdpsol --output newstuff/2018111040_1.policy  newstuff/2018111040_1.pomdp > newstuff/2018111040_1.out
echo "Second done"
./pomdpsol --output newstuff/2018111040_2.policy  newstuff/2018111040_2.pomdp > newstuff/2018111040_2.out
echo "Third done"
./pomdpsol --output newstuff/2018111040_3.policy  newstuff/2018111040_3.pomdp > newstuff/2018111040_3.out
echo "Fourth done"
./pomdpeval --simLen 100 --simNum 1000 --policy-file newstuff/2018111040_0.policy newstuff/2018111040_0.pomdp > newstuff/2018111040_0.eval 
echo "Fifth done"
./pomdpeval --simLen 100 --simNum 1000 --policy-file newstuff/2018111040_1.policy newstuff/2018111040_1.pomdp > newstuff/2018111040_1.eval 
echo "Sixth done"
./pomdpeval --simLen 100 --simNum 1000 --policy-file newstuff/2018111040_2.policy newstuff/2018111040_2.pomdp > newstuff/2018111040_2.eval 
echo "Seventh done"
./pomdpeval --simLen 100 --simNum 1000 --policy-file newstuff/2018111040_3.policy newstuff/2018111040_3.pomdp > newstuff/2018111040_3.eval 
