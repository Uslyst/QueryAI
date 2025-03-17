using ReaLTaiizor.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static QueryAI.AIModeEnum;

namespace QueryAI
{
    class AIModeManager
    {
        private readonly Dictionary<HopeRadioButton, AIMode> ModelModeMap;
        private readonly MainForm _mainForm;
        public AIModeManager(MainForm mainForm)
        {
            _mainForm = mainForm;
            ModelModeMap = InitAIModeMap();          
        }
  
        private Dictionary<HopeRadioButton, AIMode> InitAIModeMap()
        {
            Dictionary<HopeRadioButton, AIMode> map = new Dictionary<HopeRadioButton, AIMode>
            {
                { _mainForm.radioDirect, AIMode.Direct },
                { _mainForm.radioDetailed, AIMode.Detailed },
                { _mainForm.radioFree, AIMode.Free },
            };
            return map;
        }

        public AIMode GetModelMode()
        {
            foreach (var kvp in ModelModeMap)
            {
                var radio = kvp.Key;
                if (radio.Checked)
                {
                    return kvp.Value;
                }
            }
            return AIMode.Direct;
        }
    }
}
