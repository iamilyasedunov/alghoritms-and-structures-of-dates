{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from collections import deque\n",
    "\n",
    "def get_dirs(path):\n",
    "    directories = os.listdir(path) #строка с папками текущей директории\n",
    "    new_dirs = []\n",
    "    for i in directories:\n",
    "        if bool((os.path.isdir(os.getcwd() + '\\\\' + i)) == True) and (i != '.ipynb_checkpoints'): #если в имени нет точки - добавляем в список директорий\n",
    "            new_dirs.append(os.getcwd() + '\\\\' + i)\n",
    "    return(new_dirs)\n",
    "\n",
    "def insert_in_q(q, path):\n",
    "    dirs = os.listdir(path) \n",
    "    for i in dirs:\n",
    "        if (i != '.ipynb_checkpoints') and bool((os.path.isdir(path + '\\\\' + i)) == True):\n",
    "            #i = i[-1]\n",
    "            q.append(path + '\\\\' + i)\n",
    "    return q\n",
    "\n",
    "r = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D:\\bobo_town\\bobo_town\\4\\1 Bobo is here!\n",
      "Приколы от Бобо\n"
     ]
    }
   ],
   "source": [
    "q = deque()\n",
    "#Next = os.getcwd() #адрес начальной директории\n",
    "Next = 'D:\\\\bobo_town'\n",
    "q.append(Next)\n",
    "while(q):\n",
    "    Next = q.popleft()       #bfs\n",
    "    #Next = q.pop()            #dfs\n",
    "    if 'bobo.txt' in os.listdir(Next):\n",
    "        print(Next, 'Bobo is here!')\n",
    "        q.clear()\n",
    "    else:\n",
    "        insert_in_q(q, Next)\n",
    "        #print(q)\n",
    "with open(Next + '/bobo.txt','r') as myfile:\n",
    "    print(myfile.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
