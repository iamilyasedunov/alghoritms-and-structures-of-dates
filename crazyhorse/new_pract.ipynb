{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "fname = \"data.txt\"\n",
    "with open(fname) as f: \n",
    "    nx,ny = [int(p) for p in f.readline().split()] ##размеры поля\n",
    "    hx,hy = [int(p) for p in f.readline().split()] ##координаты коня\n",
    "    ex,ey = [int(p) for p in f.readline().split()] ##координаты жрачки\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9.219544457292887 9992 9993 6661\n"
     ]
    }
   ],
   "source": [
    "from scipy.spatial import distance\n",
    "_p = distance.euclidean\n",
    "\n",
    "tx, ty, level = hx,hy,0\n",
    "while(_p((tx,ty),(ex, ey)) >= _p((1,1),(8, 8))):\n",
    "    if tx<=ex and ty<=ey: #первая четверть относительно tx,ty \n",
    "        if _p((tx+2,ty+1),(ex, ey)) < _p((tx+1,ty+2),(ex, ey)):\n",
    "            tx=tx+2  \n",
    "            ty=ty+1\n",
    "        else: \n",
    "            tx=tx+1\n",
    "            ty=ty+2\n",
    "        \n",
    "    if tx>=ex and ty<=ey: #вторая четверть относительно tx,ty\n",
    "        if _p((tx-1 ,ty+2),(ex, ey)) < _p((tx-2,ty+1),(ex, ey)):\n",
    "            tx=tx-1         \n",
    "            ty=ty+2\n",
    "        else: \n",
    "            tx=tx-2\n",
    "            ty=ty+1\n",
    "        \n",
    "\n",
    "    if tx>=ex and ty>=ey: #третья четверть относительно tx,ty\n",
    "        if _p((tx-1 ,ty-2),(ex, ey)) < _p((tx-2,ty-1),(ex, ey)):\n",
    "            tx=tx-1           \n",
    "            ty=ty-2\n",
    "        else: \n",
    "            tx=tx-2\n",
    "            ty=ty-1\n",
    "        \n",
    "        \n",
    "\n",
    "    if tx<=ex and ty>=ey: #четвертая четверть относительно tx,ty\n",
    "        if _p((tx+2 ,ty-1),(ex, ey)) < _p((tx+1,ty-2),(ex, ey)):\n",
    "            tx=tx+2           #шаг вправо вверх\n",
    "            ty=ty-1\n",
    "        else: \n",
    "            tx=tx+1\n",
    "            ty=ty-2\n",
    "        \n",
    "    level+=1\n",
    "\n",
    "print(_p((tx,ty),(ex,ey)), tx, ty, level)\n",
    "\n",
    "begin = [tx, ty, level]\n",
    "tx_p, ty_p = tx,ty"
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
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myappend(steps, n_steps):\n",
    "    t = True\n",
    "    for i in range(len(n_steps)):\n",
    "        tx, ty, level = n_steps[i]\n",
    "        if tx>0 and ty>0 and t and(level != -1):\n",
    "            steps.append([tx, ty, level])\n",
    "    return steps\n",
    "\n",
    "\n",
    "def possible_step(X):      #находим координаты коня на след ходе, которые должны быть неотрицательны\n",
    "    kx, ky, level = X\n",
    "    ans_normal = []\n",
    "    ans = [[kx-2,ky-1],[kx-2,ky+1],[kx-1,ky+2],[kx-1,ky-2],[kx+1,ky+2],[kx+1,ky-2],[kx+2,ky+1],[kx+2,ky-1]]\n",
    "    for i in range(len(ans)):\n",
    "        tx, ty = ans[i]\n",
    "        \n",
    "        if (tx>0 and ty>0)and(tx!=hx or ty!=hy)and(tx<=nx and ty<=ny) and(level != -1):\n",
    "            arg = [[tx, ty, level+1]]\n",
    "            myappend(ans_normal, arg)\n",
    "    return(ans_normal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stop [9999, 9999, 6666]\n"
     ]
    }
   ],
   "source": [
    "list_of_steps = []\n",
    "list_of_steps = myappend(list_of_steps, possible_step(begin))\n",
    "f = True\n",
    "#print(list_of_steps,'========',begin)\n",
    "j=0\n",
    "while(f==True):\n",
    "    #print(list_of_steps, j, '----\\n')\n",
    "\n",
    "    if list_of_steps[j][0]==ex and list_of_steps[j][1]==ey:\n",
    "        print('stop! ',list_of_steps[j][2], list_of_steps[j], f)\n",
    "        f = False    \n",
    "    #print(list_of_steps,'--------\\n')\n",
    "    else:\n",
    "        newarr = possible_step(list_of_steps[j])\n",
    "        for i in range(len(newarr)):\n",
    "            if newarr[i] in list_of_steps:\n",
    "                newarr[i][2] = -1\n",
    "            if newarr[i][0] == ex and newarr[i][1]==ey:\n",
    "                print('stop', newarr[i])\n",
    "                f = False\n",
    "         \n",
    "    list_of_steps = myappend(list_of_steps, newarr)       \n",
    "    j=j+1\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '1 2'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-be7b1e46616d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '1 2'"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "d = []\n",
    "x = str(input())\n",
    "x.split()\n",
    "a\n",
    "b =  int(input())\n",
    "\n",
    "print(n, x, a, b)"
   ]
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
