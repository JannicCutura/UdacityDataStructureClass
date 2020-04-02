
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_paths = []

    if suffix[0] != ".":
        print("Warning! Suffix does not contain a delimiter (dot symbol)")

    if not os.path.exists(path):
        print("This path does not exist")
        return
    else:
        elements_in_path = os.listdir(path)


        folders=[]
        for element in elements_in_path:
            if os.path.isfile(path + "/" + element):
                if element.endswith(".c"):
                    files_with_paths.append(path+"/"+element)
            if os.path.isdir(path + "/" + element):
                folders.append(element)
        for folder in folders:
              files_with_paths.extend(find_files(suffix = suffix, path = path+"/"+folder))
    return files_with_paths


## change the variable below, such that it runs on your system
# this assume that you have the testdir folder in the folder where you have the problem_2.py script
projectfilespath = 'C:/Users/janni/Dropbox/university/13 Semester bis zum Lebensende/2020_03 Udacity Data Structures Class/Github/Project 1 Show me the data structures/'


## Some test cases

# test case 1: Your test case from the exceercise
print(find_files(".c", projectfilespath+'testdir'))
# works

# test case 2: a non-existent directory
print(find_files(".c", projectfilespath+'testdir2'))
# "This path does not exist"

# test case 3: Suppose we forgot the "." in the suffix
print(find_files("r", projectfilespath+'testdir2'))
# "This path does not exist"


