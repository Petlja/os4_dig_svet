Променљиве вредности
====================

Програми које си до сада радио извршавали су се одједном, без прекида. Покренеш програм и он уради све што треба. Међутим, често је
потребно да током извршавања програма убацујеш неке додатне податке како би програм знао шта да ради. 
Ако унесеш једну вредност - програм избаци један резултат. Другу вредност - врати неки други резултат.

У програму могу да постоје и вредности које нису исте током целог извршавања програма. Њих називамо **променљиве**.

.. questionnote::

 Које све вредности могу бити променљиве?
 
Променљиве могу бити вредности које дајеш програму да помоћу њих ради. Променљиве могу да буду и резултати које избацује програм.
Неке вредности могу да се мењају у самом програму. На пример, имаш неки бројач лоптица који промени вредност сваки пут када Карел узме неку лоптицу...

Погледај следећи пример. 

Пример 11
---------

У лавиринту је мрак. Карел не зна колико још корака треба да направи. Потребно је да му кажеш колико корака треба да направи и колико лоптица треба да узме са гомиле.
Сваки пут када се покрене програм, Карел ће се наћи у другом тунелу, број корака које треба да направи и број лоптица које треба да сакупи биће другачији - **променљив** је.
Влајко је саставио програм на следећи начин:

.. blockly-karel:: p551
  :categories:

  {
      setup: function() {
	  function random(n) {
              return Math.floor(n * Math.random());
           }
            var world = new World(6, 2);
			var N = 1 + random(5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBalls(N, 1, N);
            var robot = new Robot();
			var domXml = '<xml xmlns="https://developers.google.com/blockly/xml">\n  <variables>\n    <variable id="%L[D?/aos7ze,JVJVa=3">K</variable>\n    <variable id="PFq:s/Soj9)3wd@q[B)n">L</variable>\n  </variables>\n  <block type="variables_set" id="1V0Vh[sh?2L%)~#f^I7(" x="37" y="120">\n    <field name="VAR" id="%L[D?/aos7ze,JVJVa=3">K</field>\n    <value name="VALUE">\n      <block type="number_prompt" id="]f;)X;LI#UDlOgb_^_y9">\n        <field name="PROMPT">Колико корака треба да направим?</field>\n      </block>\n    </value>\n    <next>\n      <block type="variables_set" id=".DZYRD_t1WSmP(h.({UH">\n        <field name="VAR" id="PFq:s/Soj9)3wd@q[B)n">L</field>\n        <value name="VALUE">\n          <block type="number_prompt" id="zqMb=yWF)NKU#}(Imf~h">\n            <field name="PROMPT">Колико лопти треба да сакупим?</field>\n          </block>\n        </value>\n        <next>\n          <block type="controls_repeat_ext" id="HVj_-S:ZqPZ0#%T_XNMt">\n            <value name="TIMES">\n              <block type="variables_get" id=";}!x!%k_bA%ilK-SCiTV">\n                <field name="VAR" id="%L[D?/aos7ze,JVJVa=3">K</field>\n              </block>\n            </value>\n            <statement name="DO">\n              <block type="move" id="|xHWoP9*cLj4{mSyeA#D"></block>\n            </statement>\n            <next>\n              <block type="controls_repeat_ext" id="HH.`lhRf@}vxJ#{q!`|!">\n                <value name="TIMES">\n                  <block type="variables_get" id="*5OLeNWLbN0E3b9#9J2A">\n                    <field name="VAR" id="PFq:s/Soj9)3wd@q[B)n">L</field>\n                  </block>\n                </value>\n                <statement name="DO">\n                  <block type="pick_up" id="2NBp(B@@[75*]~MnN:}y"></block>\n                </statement>\n              </block>\n            </next>\n          </block>\n        </next>\n      </block>\n    </next>\n  </block>\n</xml>';
			return {world: world, robot: robot, domXml:domXml};
      },

        isSuccess: function(robot, world) {
          for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }           
  }
  
.. infonote::

 Када је у програму нека вредност променљива, можеш уместо ње да користиш неко слово или реч. 

Наравно, програму мораш да кажеш која ће вредност бити у ту реч сачувана.

Пример 12
---------

Карел је наишао на две гомиле са лоптицама. Помози му да сакупи укупно десет лоптица! Изабери колико желиш лоптица са које гомиле. 

.. blockly-karel:: p552
  :categories:
  
  {
      setup: function() {
          var world = new World(3, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          world.putHiddenNumberOfBalls(3, 1, 10);
          world.putHiddenNumberOfBalls(2, 1, 10);
          var robot = new Robot();
		  var domXml = '<xml xmlns="https://developers.google.com/blockly/xml">\n  <variables>\n    <variable id="AwA#],.@SY)1,_pSLBu!">А</variable>\n    <variable id="LWGIfI]hm.|e96X-!mAD">Б</variable>\n  </variables>\n  <block type="move" id="*N6bKICtyW#)f[%z1m_d" x="10" y="28">\n    <next>\n      <block type="variables_set" id="/VSq)TV?MPn+Z6g7xoGq">\n        <field name="VAR" id="AwA#],.@SY)1,_pSLBu!">А</field>\n        <value name="VALUE">\n          <block type="number_prompt" id="KSj.C6$c{t%TwApinU)D">\n            <field name="PROMPT">Колико лоптица да узмем?</field>\n          </block>\n        </value>\n        <next>\n          <block type="controls_repeat_ext" id="-T2},szpR=BNy?cAHX}o">\n            <value name="TIMES">\n              <block type="variables_get" id="?!Q}y,H,2k}=*fQsv/cl">\n                <field name="VAR" id="AwA#],.@SY)1,_pSLBu!">А</field>\n              </block>\n            </value>\n            <statement name="DO">\n              <block type="pick_up" id="MJdAUUYRh9^VDi3nl|]k"></block>\n            </statement>\n            <next>\n              <block type="move" id="K:kAx8)$hqm:%*$F_T2Z">\n                <next>\n                  <block type="variables_set" id="G6=0Sg8!aMc3T7A3U6a.">\n                    <field name="VAR" id="LWGIfI]hm.|e96X-!mAD">Б</field>\n                    <value name="VALUE">\n                      <block type="number_prompt" id=";4*niH%fw^{ZO(W*Dpve">\n                        <field name="PROMPT">Колико лоптица да узмем?</field>\n                      </block>\n                    </value>\n                    <next>\n                      <block type="controls_repeat_ext" id="EC60.4U#,$d^@)~uWnC:">\n                        <value name="TIMES">\n                          <block type="variables_get" id="rObm[h0qKIDy_jdXKV~b">\n                            <field name="VAR" id="LWGIfI]hm.|e96X-!mAD">Б</field>\n                          </block>\n                        </value>\n                        <statement name="DO">\n                          <block type="pick_up" id="vZ])t8Pe3EEK,@]=l~gv"></block>\n                        </statement>\n                        <next>\n                          <block type="text_print" id="Lx@eZn.yG-2O~{xqWD,Z">\n                            <value name="TEXT">\n                              <block type="math_arithmetic" id="iV;fc(p:VW2ID]_2@u`8">\n                                <field name="OP">ADD</field>\n                                <value name="A">\n                                  <block type="variables_get" id="D/E:O6|PQk[,YPx}O7ta">\n                                    <field name="VAR" id="AwA#],.@SY)1,_pSLBu!">А</field>\n                                  </block>\n                                </value>\n                                <value name="B">\n                                  <block type="variables_get" id="7oFeyTKyK,^^*:/!USS;">\n                                    <field name="VAR" id="LWGIfI]hm.|e96X-!mAD">Б</field>\n                                  </block>\n                                </value>\n                              </block>\n                            </value>\n                          </block>\n                        </next>\n                      </block>\n                    </next>\n                  </block>\n                </next>\n              </block>\n            </next>\n          </block>\n        </next>\n      </block>\n    </next>\n  </block>\n</xml>';
		  return {world: world, robot: robot, domXml:domXml};
      },

       isSuccess: function(robot, world) {
           return robot.getBalls() == 10;
      }
  }
  
.. questionnote::

 Пажљиво погледај претходна два програма и својим речима испричај како и шта они раде! Којим су словима/речима обележене променљиве вредности у првом, а којим у другом примеру?
 