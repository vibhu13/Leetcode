/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    
    public HashMap<Node, Node> map = new HashMap<>();
    
    public Node cloneGraph(Node node) {    
        //return bfs(node);
        return dfs(node);
    }
    
    private Node dfs(Node node){
        if (node == null) 
            return null;
        
        if (map.containsKey(node)) 
            return map.get(node);
        
        Node replicaNode = new Node(node.val, new ArrayList<Node>());
        map.put(node, replicaNode);
        
        for (Node neighbor : node.neighbors){ 
            Node temp = dfs(neighbor);
            replicaNode.neighbors.add(temp);
        }
        
        return replicaNode;
    }
    
    private Node bfs(Node node){        
        if (node == null) 
            return null;
        Node replicaNode = new Node(node.val);
        //<K,V> <Original,Replica> Mapping..
        //<K,V> <Integer,Replica> Mapping.. could also be stored..
        HashMap<Node, Node> map = new HashMap<>();
        map.put(node, replicaNode);
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            for (Node neighbor : current.neighbors) {
                if (!map.containsKey(neighbor)) {
                    Node localReplicaNode = new Node(neighbor.val);
                    map.put(neighbor, localReplicaNode);
                    queue.add(neighbor);
                }
                map.get(current).neighbors.add(map.get(neighbor));
            }
        }
        return replicaNode;
    }
}
