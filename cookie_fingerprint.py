#!/usr/local/bin/python

# Find all cookies that share common fingerprints

class CFNode(object):
	COOKIE = "COOKIE"
	FINGERPRINT = "FINGERPRINT" 

	def __init__(self, value, nodetype):
		self.value = value
		self.nodetype = nodetype 
		self.visited = False
		self.links = {}


	def link(self, node):
		val = node.value
		if not self.links.get(val):
			self.links[val] = node
		if not node.links.get(self.value):
			node.links[self.value] = self


	def __str__(self):
		return "%s: %r -> %r" % (self.nodetype, self.value, self.links.keys())


def get_common(root):
	"Iterative approach BFS"
	if not root:
		return []
	queue = []
	common = []
	queue.append(root)
	while len(queue) > 0:
		cur_node = queue.pop(0)
		if cur_node.nodetype == CFNode.COOKIE and cur_node.visited == False:
			common.append(cur_node)
		cur_node.visited = True
		for n in cur_node.links.values():
			if n.visited == False:
				queue.append(n)
	return common	


def get_common2(root):
	"Recursive approach"
	if not root:
		return []
	if len(root.links.values()) == 0:
		if root.nodetype == COOKIE:
			return [root]
		else:
			return []
	common = []
	for n in root.links.values():
		common.extend(get_common2(n))
	return common


if __name__ == "__main__":
	n_a = CFNode("A", CFNode.COOKIE)
	n_b = CFNode("B", CFNode.COOKIE)
	n_c = CFNode("C", CFNode.COOKIE)
	n_d = CFNode("D", CFNode.COOKIE)
	n_1 = CFNode("1", CFNode.FINGERPRINT)
	n_2 = CFNode("2", CFNode.FINGERPRINT)
	n_3 = CFNode("3", CFNode.FINGERPRINT)

	# Test 1
	n_a.link(n_1)
	n_b.link(n_1)
	n_b.link(n_2)
	n_b.link(n_3)
	n_c.link(n_3)
	n_d.link(n_2)
	n_d.link(n_3)

	# Test 2
	# n_a.link(n_1)
	# n_a.link(n_2)
	# n_b.link(n_1)
	# n_b.link(n_2)
	# n_c.link(n_1)

	print n_a
	print n_b
	print n_c
	print n_d
	print n_1
	print n_2
	print n_3
	common = get_common(n_a)
	# common = get_common2(n_a)
	print "Common %r" % [x.value for x in common]






