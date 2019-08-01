import numpy
import math
import random

from mwmatching import *

# Number of iterations (change as necessary)
iters = 100000

# Distance when running the shortest path
def distance(a, b, adj):
   return -math.log(abs(adj[a][b]))

# Centrality function (subject to change)
# a is correlation with left neighbor
# b is correlation with right neighbor
def f(a, b):
   return (a+b)/2.0


class MWMPlugin:
   def input(self, filename):
      filestuff = open(filename, 'r')

      # Get the first line (names)
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if ('\"\"' in self.bacteria):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      inf = float("infinity")
      # Make the identity matrix I
      # and the adjacency matrix A
      # and the positive matrix P
      # and the negative matrix N
      self.m = []
      for line in filestuff:
         mc = []
         contents = line.split(',')
         for i in range(1, self.n+1):
            value = float(contents[i])
            mc.append(value)
         self.m.append(mc)

      # Check to make sure all entries (i, i) are 0
      for i in range(self.n):
         self.m[i][i] = 0


   def run(self):
      # Assemble tuples for mwmatching
      # Inefficient but ok for now
      self.edges = []
      for i in range(self.n):
        for j in range(i+1, self.n):
           if (i != j and self.m[i][j] != 0):
              self.edges.append((i, j, distance(i,j,self.m)))

      self.mwm = maxWeightMatching(self.edges)

   def output(self, filename):
      #print len(mwm)
      #print mwm
      #print n
      count = 0
      for i in range(len(self.mwm)):
         if (self.mwm[i] != -1):
            count += 1

      print("Driver Nodes: "+str(count)+" out of "+str(self.n))

      for i in range(len(self.edges)):
          tmp = self.edges[0]
          self.edges.remove(tmp)
          mwm2 = maxWeightMatching(self.edges)
          count2 = 0 
          for j in range(len(mwm2)):
             if (mwm2[j] != -1):
                count2 += 1
          if (count2 > count):
             print("Possible Critical Edge: "+self.bacteria[tmp[0]].strip()+"-"+self.bacteria[tmp[1]].strip()+" "+str(count2))
          #else:
          #   print "Non-Critical Edge: ", tmp, " ", count2
          self.edges.append(tmp)


