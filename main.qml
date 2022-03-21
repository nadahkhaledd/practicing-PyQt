import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow
{
    id: mainWindow
    height: 160
    width: 300

    Item
    {
        id: page
        visible: true
        width: parent.width

        Rectangle
        {
            height: 160
            color: "#eab676"

            Text
            {
                text: "Regular text"
                height: 50
                width: parent.width
                font.pixelSize: 12

            }
        }
    }
}