class Solution {
public:
    void dfs(vector<vector<char>>&grid,int i,int j,int r,int c){
        if (i < 0 || i >= r || j < 0 || j >= c || grid[i][j] != '1')
            return;
        
        if(grid[i][j] == '0') return;
        
        grid[i][j] = '2';
        
        dfs(grid,i+1,j,r,c);
        dfs(grid,i-1,j,r,c);
        dfs(grid,i,j+1,r,c);
        dfs(grid,i,j-1,r,c);
    }

    int numIslands(vector<vector<char>> &grid)
    {
	    int ct = 0;
	    int row = grid.size();
	    int col = grid[0].size();

	    for(int i=0;i<row;i++){
		    for(int j=0;j<col;j++){
			    if(grid[i][j] == '1'){
				    dfs(grid,i,j,row,col);
				    ct+=1;
			    }
		    }
	    }
	    return ct;
    }
};