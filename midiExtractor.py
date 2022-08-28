import pretty_midi

midi_data = pretty_midi.PrettyMIDI('FireFlies.mid')
filename= "FireFlies.ini"

PureRightHandNotes=[]
PureRightHandDuration=[]
PureRightHandStart=[]
PureRightHandStop=[]

PureLeftHandNotes=[]
PureLeftHandDuration=[]
PureLeftHandStart=[]
PureLeftHandStop=[]
notenow = None

class Note:
    def __init__(self,side,note,duration,start,stop):
        self.side =side
        self.note=note
        self.duration =duration
        self.start =start
        self.stop = stop

NoteArray = []
for instrument in midi_data.instruments:
    for noteindex in range(len(instrument.notes)):

        print(instrument.notes[noteindex])
        if noteindex > 0 and (instrument.notes[noteindex].start == instrument.notes[noteindex-1].start):

           NoteArray.append(Note("Left",pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                 instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                 instrument.notes[noteindex].start,
                                 instrument.notes[noteindex].end))
         

        elif noteindex < len(instrument.notes)-1 and (instrument.notes[noteindex].start == instrument.notes[noteindex+1].start):

            NoteArray.append(Note("Right", pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                  instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                  instrument.notes[noteindex].start,
                                  instrument.notes[noteindex].end))
        else:
        

            if len(NoteArray)>0 and NoteArray[-1].stop > instrument.notes[noteindex].start:
                if NoteArray[-1].side == "Left":
                    NoteArray.append(Note("Right", pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                          instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                          instrument.notes[noteindex].start,
                                          instrument.notes[noteindex].end))
                elif NoteArray[-1].side == "Right":
                    NoteArray.append(Note("Left", pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                          instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                          instrument.notes[noteindex].start,
                                          instrument.notes[noteindex].end))
            else:
                if instrument.notes[noteindex].pitch >=60:
                    NoteArray.append(Note("Right", pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                      instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                      instrument.notes[noteindex].start,
                                      instrument.notes[noteindex].end))
                if instrument.notes[noteindex].pitch < 60:
                        NoteArray.append(Note("Left", pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch),
                                              instrument.notes[noteindex].end - instrument.notes[noteindex].start,
                                              instrument.notes[noteindex].start,
                                              instrument.notes[noteindex].end))
          

for note in NoteArray:
    if note.side == "Left":
        PureLeftHandNotes.append(note.note)
        PureLeftHandDuration.append(note.duration)
        PureLeftHandStart.append(note.start)
        PureLeftHandStop.append(note.stop)
    elif note.side == "Right":
        PureRightHandNotes.append(note.note)
        PureRightHandDuration.append(note.duration)
        PureRightHandStart.append(note.start)
        PureRightHandStop.append(note.stop)


textfile = open(filename,"w")
textfile.write("[Song]\n")
textfile.write("NotesR=")
for element in PureRightHandNotes:

    textfile.write(str(element)+",")



textfile.write("\nDurationR=")
for element in PureRightHandDuration:

   textfile.write(str(element) + ",")

textfile.write("\nStartR=")
for element in PureRightHandStart:

   textfile.write(str(element) + ",")

textfile.write("\nStopR=")
for element in PureRightHandStop:

    textfile.write(str(element) + ",")






textfile.write("\nNotesL=")
for element in PureLeftHandNotes:

    textfile.write(str(element) + ",")



textfile.write("\nDurationL=")
for element in PureLeftHandDuration:

    textfile.write(str(element) + ",")

textfile.write("\nStartL=")
for element in PureLeftHandStart:

   textfile.write(str(element) + ",")

textfile.write("\nStopL=")
for element in PureLeftHandStop:

   textfile.write(str(element) + ",")






textfile.close()


