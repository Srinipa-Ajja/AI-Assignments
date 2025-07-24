class state:
	def __init__(self,s0, s1,s2,s3,s4,s5,s6,s7,s8):
		self.s0=s0
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4=s4
		self.s5=s5
		self.s6=s6
		self.s7=s7
		self.s8=s8
	def __eq__(self, other):
		return isinstance(other, state) and (
        self.s0 == other.s0 and self.s1 == other.s1 and self.s2 == other.s2 and
        self.s3 == other.s3 and self.s4 == other.s4 and self.s5 == other.s5 and
        self.s6 == other.s6 and self.s7 == other.s7 and self.s8 == other.s8
    )

	        
	def goalstate(self):
	    return self.s0==self.s1==self.s2=='>' and self.s6==self.s7==self.s8=='<' and self.s3==self.s4==self.s5=='_'

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
	
	def __hash__(self):
		return hash((self.s0,self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8))
		
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

	def bfs(self):
		open=[(self,None)]
		closed=[]
		while open:
			pair=open.pop(0)
			n,parent=pair
			if n.goalstate():
				path=self.reconstruct(pair,closed)
				path.reverse()
				print("bfs path:")
				c=0
				for i in path:
					c=c+1
					print(c,i)
				return path
			else:
				closed.append(pair)
				children=n.moveGen()
				nnode=self.remove(open,closed,children)
				for i in nnode:
					open.append((i,n))
		print("no path")
		return []

	def dfs(self):
		open=[(self,None)]
		closed=[]
		while open:
			pair=open.pop(0)
			n,parent=pair
			if n.goalstate():
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
	
	def moveGen(self):
		children=[]
		for i in range(9):
			items=[self.s0,self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8]
			temp=items.copy()
			if items[i]=='_':
				if i>=1 and items[i-1]=='<':
					items[i]='<'
					items[i-1]='_'
					child=state(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
					children.append(child)
					items=temp.copy()
				if i>=2 and items[i-2]=='<': 
					items[i]='<'
					items[i-2]='_'
					child=state(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
					children.append(child)
					items=temp.copy()
				if i<=7 and items[i+1]=='>':
					items[i]='>'
					items[i+1]='_'
					child=state(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
					children.append(child)
					items=temp.copy()
				if i<=6 and items[i+2]=='>':
					items[i]='>'
					items[i+2]='_'
					child=state(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
					children.append(child)
		return children
	
	
	
	def __str__(self):
		return f"{self.s0} {self.s1} {self.s2} {self.s3} {self.s4} {self.s5} {self.s6} {self.s7} {self.s8}"
    
s=state('_','<','<','<','_','>','>','>','_')
s.bfs()
s.dfs()