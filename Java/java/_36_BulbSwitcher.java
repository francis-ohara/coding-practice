/*  Link: https://leetcode.com/problems/bulb-switcher/
    Task:
        There are n bulbs that are initially off. You first tum on all the bulbs, then you turn off every second bulb.
        On the third round, you toggle every third bulb (tuming on if it's off or turning off if it's on). For the ith round,
        you toggle every i bulb. For the nth round, you only toggle the last bulb.
        Retum the number of bulbs that are on after n rounds.
 */

class Solution {
        
  public int bulbSwitch(int n) {
        boolean[] bulbs = new boolean[n];
        int nBulbsOn = 0;
        // 1st & 2nd round
        for (int i=0; i < n; i++){
            if ((i+1) % 2 == 1)
                bulbs[i] = true;
        }

        // remaining rounds
        for (int round = 3; round <= n; round++) {
            for (int j = 0; j < n; j++){
                if ((j + 1) % round == 0)
                    bulbs[j] = !bulbs[j];
                
            }
        }
       
        // count number of bulbs on
        for (int i = 0; i < n; i ++)
            nBulbsOn += bulbs[i]==true?1:0;
        
        return nBulbsOn;
    }
}