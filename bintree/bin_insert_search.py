{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "data =  4 | left =  <__main__.node object at 0x0000022BFF84DDA0> | right =  <__main__.node object at 0x0000022BFF84DCC0> \n",
      "\n",
      "data =  3 | left =  <__main__.node object at 0x0000022BFF84AEF0> | right =  None \n",
      "\n",
      "data =  2 | left =  None | right =  None \n",
      "\n",
      "data =  8 | left =  <__main__.node object at 0x0000022BFF84DE80> | right =  <__main__.node object at 0x0000022BFF7E9E80> \n",
      "\n",
      "data =  6 | left =  None | right =  <__main__.node object at 0x0000022BFF7E9400> \n",
      "\n",
      "data =  7 | left =  None | right =  None \n",
      "\n",
      "data =  16 | left =  None | right =  None \n",
      "\n"
     ]
    }
   ],
   "source": [
    "class Tree(object):\n",
    "    def __init__(self):\n",
    "        self.data=None\n",
    "        self.left=None\n",
    "        self.right=None\n",
    "    def insert(self, x, root):\n",
    "        if root==None:\n",
    "            t=node(x)\n",
    "            t.data=x\n",
    "            t.right=None\n",
    "            t.left=None\n",
    "            root=t\n",
    "            return root\n",
    "        elif x<root.data:\n",
    "            root.left=self.insert(x, root.left)\n",
    "        else:\n",
    "            root.right=self.insert(x, root.right)\n",
    "        return root\n",
    "        \n",
    "    def printTree(self, t):\n",
    "        if t==None:\n",
    "            return\n",
    "\n",
    "        self.printTree(t.left)\n",
    "        print(t.data)\n",
    "        self.printTree(t.right)\n",
    "\n",
    "class node(object):\n",
    "    def __init__(self, x):\n",
    "        self.x=x\n",
    "\n",
    "def search(root, low, high):\n",
    "        if root == None:\n",
    "            return\n",
    "        if (low <= root.data <= high):\n",
    "            print('data = ', root.data,'| left = ', root.left, '| right = ', root.right, '\\n')\n",
    "        \n",
    "        search(root.left, low, high)\n",
    "        search(root.right, low, high) \n",
    "        \n",
    "bt=Tree()\n",
    "root=None\n",
    "\n",
    "root = bt.insert(4, root)\n",
    "root = bt.insert(3, root)\n",
    "root = bt.insert(8, root)\n",
    "root = bt.insert(2, root)\n",
    "root = bt.insert(6, root)\n",
    "root = bt.insert(7, root)\n",
    "root = bt.insert(16, root)\n",
    "\n",
    "#n=int(input())\n",
    "#a=[]\n",
    "\n",
    "#for i in range(n):\n",
    "#    a.append(int(input()))\n",
    "\n",
    "#for i in range(n):\n",
    "#    root=bt.insert(a[i], root)\n",
    "#mainRoot = bt.insert(a[0], root)\n",
    "search(root, 2, 16)\n",
    "\n",
    "  "
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
