using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QueryAI
{
    public class AIExchange
    {
        readonly PythonBridge _bridge;
        public AIExchange(PythonBridge bridge)
        {
            _bridge = bridge ?? throw new ArgumentNullException(nameof(bridge));
        }
        public string SendAndRecieve(string userInput, AIModeEnum.AIMode mode)
        {
            string message = $"[{mode}] {userInput}";
            var client = _bridge.GetClient();
            var stream = _bridge.GetStream();

            byte[] data = Encoding.UTF8.GetBytes(message); // UTF8 for accents "á, ç, ã, etc"
            stream.Write(data, 0, data.Length);
            
            byte[] buffer = new byte[1024];
            int bytesRead = stream.Read(buffer, 0, buffer.Length);

            return Encoding.UTF8.GetString(buffer);
        }       
    }
}
