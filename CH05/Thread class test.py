{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "import time\n",
    "\n",
    "class MyThread(threading.Thread):\n",
    "    def __init__(self,msg):\n",
    "        super.__init__(self)\n",
    "        self.msg = msg\n",
    "        self.daemon = True\n",
    "        \n",
    "    def run(self):\n",
    "        while True:\n",
    "            time.sleep(1)\n",
    "            print(self.msg)\n",
    "            \n",
    "            "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
