def is_sum_equal(*elements):
    result=elements[0]
    remaining=elements[1:]
    sum_of_elements=sum(remaining)
    if result==sum_of_elements:
        return True
    return False

main_node=int(input())
leftside_subnode=int(input())
rightside_subnode=int(input())
left_left_least_node=int(input())
right_left_least_node=int(input())
condition_1=is_sum_equal(leftside_subnode,left_left_least_node,right_left_least_node)
right_right_least_node=int(input())
condition_2=is_sum_equal(main_node,leftside_subnode,rightside_subnode,left_left_least_node,right_left_least_node,right_right_least_node)
is_sum_binary_tree=condition_1 and condition_2
if (is_sum_binary_tree):
    print("It is sum binary tree")
else:
    print("It is not sum binary tree")