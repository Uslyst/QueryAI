using ReaLTaiizor.Controls;
using Timer = System.Windows.Forms.Timer;
using static QueryAI.AIModeEnum;
namespace QueryAI
{


    public partial class MainForm : Form
    {
        private Timer typingTimer;
        private string textToType = "_";
        private int currentIndex = 0;
        
        private readonly AIModeManager modeManager;
        private readonly AIExchange exchange;
        public MainForm()
        {
            InitializeComponent();
            

            modeManager = new AIModeManager(this);
            PythonBridge bridge = new PythonBridge();
            exchange = new AIExchange(bridge);
            
            SetupAITypingEffect();
        }
        private void SetupAITypingEffect()
        {
            typingTimer = new Timer();
            typingTimer.Interval = 10;
            typingTimer.Tick += typingTimer_Tick;
        }
        private void EnableAITyping(string text)
        {
            labelOutput.Text = "";
            textToType = text;
            currentIndex = 0;
            typingTimer.Start();
        }
        private void typingTimer_Tick(object sender, EventArgs e)
        {
            if (currentIndex < textToType.Length)
            {
                labelOutput.Text += textToType[currentIndex];
                currentIndex++;
            }
            else
            {

                typingTimer.Stop();
            }
        }
        
        

        private void cyberButton1_Click(object sender, EventArgs e)
        {

            string userInput = textBoxUserInput.TextButton;
            if(string.IsNullOrEmpty(userInput))
            {
                return;
            }

            AIMode mode = modeManager.GetModelMode();

            string modelAnswer = exchange.SendAndRecieve(userInput, mode);
            EnableAITyping(modelAnswer);


        }



    }
}
