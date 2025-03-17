using System.Net.Sockets;

namespace QueryAI
{
    public class PythonBridge
    {
        private TcpClient client;
        private NetworkStream stream;

        public PythonBridge()
        {
            InitializePythonFile("");
            Open();
        }
        public void InitializePythonFile(string scriptName)
        {
            //Process
        }
        public TcpClient GetClient()
        {
            return client;
        }

        public NetworkStream GetStream()
        {
            return stream;
        }
        private void Open()
        {
            client = new TcpClient("127.0.0.1", 5000);
            stream = client.GetStream();
        }

        private void Close()
        {
            client.Close();
        }



    }

   
}
