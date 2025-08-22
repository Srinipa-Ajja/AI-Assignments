class state:
	a1t=5
	a2t=10
	a3t=20
	a4t=25
	def __init__ (self,u,a1,a2,a3,a4,t):
		self.u=u
		self.a1=a1
		self.a2=a2
		self.a3=a3
		self.a4=a4
		self.t=t

	def goalTest(self):
		return self.a1==self.a2==self.a3==self.a4=='r' and self.t<=60
	
	
	def moveGen(self):
		children=[]
		cost=99999
		items=["a1","a2","a3","a4"]
		if self.u=='l':
			n='r'
		else:
			n='l'
		if n=='r':
			for e in items :
				for  f in items:
					if e!=f:
						child =None
						if e=="a1" and f=="a2" and self.a1==self.a2=='l':
							child=state(n,n,n,self.a3,self.a4,self.t+state.a2t)
						elif e=="a1" and f=="a3" and self.a1==self.a3=='l':
							child=state(n,n,self.a2,n,self.a4,self.t+state.a3t)
						elif e=="a1" and f=="a4" and self.a1==self.a4=='l':
							child=state(n,n,self.a2,self.a3,n,self.t+state.a4t)
						elif e=="a2" and f=="a3" and self.a3==self.a2=='l':
							child=state(n,self.a1,n,n,self.a4,self.t+state.a3t)
						elif e=="a2" and f=="a4" and self.a4==self.a2=='l':
							child=state(n,self.a1,n,self.a3,n,self.t+state.a4t)
						elif e=="a3" and f=="a4" and self.a4==self.a3=='l':
							child=state(n,self.a1,self.a2,n,n,self.t+state.a4t)
						if child is not None and child.t<=60:
							children.append(child)	
		else:
			for e in items:
				child=  None
				if e=="a1" and self.a1=='r':
					child=state(n,n,self.a2,self.a3,self.a4,self.t+state.a1t)
				elif e=="a2" and self.a2=='r':
					child=state(n,self.a1,n,self.a3,self.a4,self.t+state.a2t)
				elif e=="a3" and self.a3=='r':
					child=state(n,self.a1,self.a2,n,self.a4,self.t+state.a3t)
				elif e=="a4" and self.a4=='r':
					child=state(n,self.a1,self.a2,self.a3,n,self.t+state.a4t)
				if child is not None and child.t<=60:
				    children.append(child)
		return children
	
	def reconstruct(self,pair,closed):
		path=[]
		dict={}
		for node,parent in closed:
			dict[node]=parent
		node,parent=pair
		path.append(node)
		while parent is not None:
			path.append(parent)
			parent=dict[parent]
		return path
	
	def remove(self,open,closed,children):
		onode=[]
		cnode=[]
		nnode=[]
		for node,parent in open:
		    	onode.append(node)
		for node,parent in closed:
		    	cnode.append(node)
		for c in children:
			if c not in onode and c not in cnode:
				nnode.append(c)
		return nnode

	def bfs(self):
		open=[(self,None)]
		closed=[]
		while open:
			pair=open.pop(0)
			n,parent=pair
			if n.goalTest():
				print("bfs path:")
				path=self.reconstruct(pair,closed)
				path.reverse()
				c=0
				for p in path:
					c=c+1
					print(c,p)
				return path
			else:
				closed.append(pair)
				children=n.moveGen()
				nnode=self.remove(open,closed,children)
				for c in nnode:
				    open.append((c,n))
		print("no path")
		return []

	def dfs(self):
		open=[(self,None)]
		closed=[]
		while open:
			pair=open.pop(0)
			n,parent=pair
			if n.goalTest():
				print("dfs path:")
				path=self.reconstruct(pair,closed)
				path.reverse()
				c=0
				for p in path:
					c=c+1
					print(c,p)
				return path
			else:
				closed.append(pair)
				children=n.moveGen()
				nnode=self.remove(open,closed,children)
				npair=[]
				for c in nnode:
					npair.append((c,n))
				open=npair+open
		print("no path")
		return
	
	def __eq__(self, other):
		return (self.u, self.a1, self.a2, self.a3, self.a4, self.t) == (other.u, other.a1, other.a2, other.a3, other.a4, other.t)

	def __hash__(self):
		return hash((self.u, self.a1, self.a2, self.a3, self.a4, self.t))

	def __str__(self):
		return f"{self.u}{self.a1}{self.a2}{self.a3}{self.a4}{self.t}"
	
s=state('l','l','l','l','l',0)
s.bfs()
s.dfs()