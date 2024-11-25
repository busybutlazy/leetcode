def counter(s:str)->int:
    num_of_word=0
    for i in range(1,len(s)):
        last_word=ord(s[i-1])
        now_word=ord(s[i])
        if s[i]=="'":
            continue
        if is_alphabet(last_word) and not is_alphabet(now_word):
            num_of_word+=1
    return num_of_word

def is_alphabet(id:int)->bool:
    return id>=65 and id<=122

s="""Step aside tropical rainforests and coral reeds — the latest hotspot to offer awe-inspiring biodiversity lies no further than your bathroom.

In a new Northwestern University-led study, microbiologists found that showeheads and toothbrushes are teeming with an extremely diverse collection of viruses — most of which have never been seen before.

Although this might sound ominous, the good news is these viruses don’t target people. They target bacteria.

The microorganisms collected in the study are bacteriophage, or “phage”, a type of virus that infects and replicates inside of bacteria. Although researchers know little about them, phage recently have garnered attention for their potential use in treating antibiotic-resistant bacterial infections. And the previously unknown viruses lurking in our bathrooms could become a treasure trove of materials for exploring those applications.

The study will be published Wednesday (Oct. 9) in the journal Frontiers in Microbiomes.

“The number of viruses that we found is absolutely wild,” said Northwestern’s Erica M. Hartmann, who led the study. “We found many viruses that we know very little about and many others that we have never seen before. It’s amazing how much untapped biodiversity is all around us. And you don’t even have to go far to find it; it’s right under our noses.”

An indoor microbiologist, Hartmann is an associate professor of civil and environmental engineering at Northwestern’s McCormick School of Engineering and a member of the Center for Synthetic Biology.

### The return of ‘Operation Pottymouth’

The new study is an offshoot of previous research, in which Hartmann and her colleagues at University of Colorado at Boulder  characterized bacteria living on toothbrushes and showerheads. For the previous studies, the researchers asked people to submit used toothbrushes and swabs with samples collected from their showerheads.

Inspired by concerns that a flushing toilet might generate a cloud of aerosol particles, Hartmann addectionately called the toothbrush study, “Operation Pottymouth.”

“This projects started as a curiosity,” Hartmann said. “We wanted to know what microbs are living in our homes. If you think about indoor environments, surfaces like tables and walls are really difficult for microbes to live on. Microbes prefer environments with water. And where is there water? Inside our showerheads and on our toothbrushes.”

### Diversity and opportunities

After characterizing bacteria, Hartmann then used DNA sequencing to examine the viruses living on those same samples. She was immediately blown away. Altogether, the samples comprised more than 600 diffent viruses — and no two samples were alike.

“We saw basically no overlap in virus types between showerhead and toothbrushes,” Hartmann said. “We also saw very little overlap between any two samples at all. Each showerhead and each toothbrush is like its own little island. It just underscores the incredible diversity of viruses out there.”

While they found few patterns among all the samples, Hartmann and her team did notice more mycobacteriophage than other types of phage. Mycobacteriophage infect mycobacteria, a pathogenic species that causes diseases like leprosy, tuberculosis and chronic lung infections. Hartmann imagines that, someday, researchers could harness mycobacteriophage to treat these infections and others.

“We could envision taking these mycobacteriophage and using them as a way to clean pathogens out of your plumbing system,” she said. “We want to look at all the functions these viruses might have and figure out how we can use them.”

### Most microbes ‘will not make us sick’

But, in the meantime, Hartmann cautions people not to fret about the invisible wildlife living within our bathrooms. Instead of grabbing for bleach, people can soak their showerheads in vinegar to remove calcium buildup or simply wash them with plain soap and water. And people should regularly replace toothbrush heads, Hartmann says. Hartmann also is not a fan of antimicrobial toothbrushes, which she said can lead to antibiotic-resistant bugs.

“Microbes are everywhere, and the vast majority of them will not make us sick, ” she said. “The more you attack them with disinfectants, the more they are likey to develop resistance or become more difficult to treat. We should all just embrace them.”

The study, “Phage communities in household-related biofilms correlate with bacterial hosts but do not associate with other environment factors,” was supported by Northwestern University."""
print(counter(s))