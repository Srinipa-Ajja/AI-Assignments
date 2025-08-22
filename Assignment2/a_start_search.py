class state:
	def __init__ (self,a,r,c):
		self.a=a
		self.r=r;
		self.c=c;
		
	def goalTest(self):
		return self.r==2 and self.c==2
		
	def moveGen(self):
		children=[]
		direc=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)];
		for i,j in direc:
			nr,nc=self.r+i,self.c+j
			if 0<=nr<3 and 0<=nc<3 and self.a[nr][nc]==0:
				child=state(self.a,self.r+i,self.c+j)
				children.append(child)
		return children
		
	def __str__(self):
		return f"({self.r},{self.c})"
		
	def __eq__(self, other):
		return self.r==other.r and self.c==other.c
	
	def reconstruct(self,pair,closed):
		path=[]
		dict={}
		for node,parent,g in closed:
			dict[node]=parent
		node,parent,g=pair
		path.append(node)
		while parent is not None:
			path.append(parent)
			parent=dict[parent]
		return path
	
	def remove(self,open,closed,children):
		onode=[]
		cnode=[]
		nnode=[]
		for node,parent,g in open:
		    	onode.append(node)
		for node,parent,g in closed:
		    	cnode.append(node)
		for c in children:
			if c not in onode and c not in cnode:
				nnode.append(c)
		return nnode
		
	def ass(self):
		open=[(self,None,0)]
		closed=[]
		while open:
			pair=min(open,key=state.f_h_g)
			n,parent,g=pair
			if n.goalTest():
				print("ass path:")
				path=self.reconstruct(pair,closed)
				path.reverse()
				c=0
				for p in path:
					c=c+1
					print(p)
					print("\n")
				return path
			else:
				closed.append(pair)
				children=n.moveGen()
				nnode=self.remove(open,closed,children)
				for c in nnode:
				    open.append((c,n,g+1))
		print("no path")
		return []
		
	@staticmethod
	def f_h_g(x):
		node,par,g=x
		h= abs(2-node.r)+abs(2-node.c)
		return h+g
	
		
	def __hash__(self):
		return hash((self.r, self.c))


a=[[0,0,0],
     [0,0,0],
     [1,1,0]];
s=state(a,0,0)
s.ass()
